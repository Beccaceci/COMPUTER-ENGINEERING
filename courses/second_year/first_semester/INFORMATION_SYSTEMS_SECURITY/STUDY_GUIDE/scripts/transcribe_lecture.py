#!/usr/bin/env python3
"""
Automated lecture transcription script for Sicurezza dei Sistemi Informativi.
Extracts audio from video, runs Whisper (large-v3-turbo with MPS GPU acceleration),
and formats the transcription into structured Markdown with timestamps in LECTURE TRANSCRIPTIONS/.
Strictly isolates temporary audio files in /tmp/ to prevent root directory pollution.
"""

import os
import sys
import argparse
import subprocess
import tempfile
import time
from datetime import datetime
from pathlib import Path

def format_timestamp(seconds: float) -> str:
    s = int(seconds)
    hh = s // 3600
    mm = (s % 3600) // 60
    ss = s % 60
    return f"{hh:02d}:{mm:02d}:{ss:02d}"

def get_audio_duration(file_path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

def extract_audio(video_path: str, output_wav: str) -> None:
    print(f"[*] Extracting 16kHz mono audio from {video_path} -> {output_wav}")
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        output_wav
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print(f"[+] Audio extraction complete.")

def transcribe_audio(
    wav_path: str,
    model_name: str = "large-v3-turbo",
    device: str = "mps",
    initial_prompt: str = ""
):
    import torch
    import whisper

    if device == "mps" and not torch.backends.mps.is_available():
        print("[!] MPS device requested but not available. Falling back to CPU.")
        device = "cpu"

    print(f"[*] Loading Whisper model '{model_name}' on device '{device}'...")
    model = whisper.load_model(model_name, device=device)
    print(f"[+] Model loaded successfully. Starting transcription...")

    # Options for robust academic transcription
    options = {
        "language": "it",
        "task": "transcribe",
        "temperature": (0.0, 0.2, 0.4, 0.6),
        "condition_on_previous_text": False,
        "compression_ratio_threshold": 2.4,
        "logprob_threshold": -1.0,
        "no_speech_threshold": 0.6,
        "fp16": False,
        "verbose": True
    }
    if initial_prompt:
        options["initial_prompt"] = initial_prompt

    start_time = time.time()
    result = model.transcribe(wav_path, **options)
    elapsed = time.time() - start_time
    print(f"[+] Transcription completed in {elapsed:.1f}s ({elapsed/60:.1f} minutes).")
    return result

def generate_markdown(
    result: dict,
    lecture_num: str,
    lecture_date: str,
    topic: str,
    source_filename: str,
    duration_sec: float,
    summary_bullets: list
) -> str:
    hours = int(duration_sec // 3600)
    minutes = int((duration_sec % 3600) // 60)
    today = datetime.now().strftime("%Y-%m-%d")

    summary_text = "\n".join(f"{i+1}. {item}" for i, item in enumerate(summary_bullets))

    md_lines = [
        f"# Sicurezza dei Sistemi Informativi — Trascrizione Lezione {lecture_num}",
        "",
        f"**Data:** {lecture_date}  ",
        f"**Docente:** Prof. Cataldo Basile  ",
        f"**Argomento:** {topic}  ",
        f"**File Sorgente:** `{source_filename}`  ",
        f"**Durata Registrazione:** ~{hours} ore e {minutes} minuti ({duration_sec:.0f} secondi)  ",
        f"**Data Trascrizione:** {today}  ",
        "",
        "---",
        "",
        "## Sommario degli Argomenti Trattati",
        "",
        summary_text,
        "",
        "---",
        "",
        "## Trascrizione Completa con Timestamp",
        ""
    ]

    for segment in result.get("segments", []):
        ts = format_timestamp(segment["start"])
        text = segment["text"].strip()
        if text:
            md_lines.append(f"**`[{ts}]`** {text}\n")

    return "\n".join(md_lines)

def main():
    parser = argparse.ArgumentParser(description="Transcribe lecture recording to structured Markdown.")
    parser.add_argument("--input-video", required=True, help="Path to input video/audio recording.")
    parser.add_argument("--output-md", required=True, help="Destination Markdown file in LECTURE TRANSCRIPTIONS/.")
    parser.add_argument("--lecture-num", required=True, help="Lecture number (e.g. 02, 03).")
    parser.add_argument("--lecture-date", required=True, help="Lecture date (e.g. '28 Settembre 2026').")
    parser.add_argument("--topic", required=True, help="Topic description.")
    parser.add_argument("--summary", nargs="+", default=[], help="Summary bullet points.")
    parser.add_argument("--model", default="large-v3-turbo", help="Whisper model name.")
    parser.add_argument("--device", default="mps", help="Device (mps or cpu).")
    parser.add_argument("--prompt", default="", help="Initial domain prompt.")

    args = parser.parse_args()

    input_path = os.path.abspath(args.input_video)
    if not os.path.exists(input_path):
        print(f"[!] Error: input file '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)

    output_path = os.path.abspath(args.output_md)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Use /tmp for scratch audio file
    temp_wav = f"/tmp/lecture_audio_{os.getpid()}_{int(time.time())}.wav"

    try:
        duration_sec = get_audio_duration(input_path)
        extract_audio(input_path, temp_wav)

        result = transcribe_audio(
            wav_path=temp_wav,
            model_name=args.model,
            device=args.device,
            initial_prompt=args.prompt
        )

        md_content = generate_markdown(
            result=result,
            lecture_num=args.lecture_num,
            lecture_date=args.lecture_date,
            topic=args.topic,
            source_filename=os.path.basename(input_path),
            duration_sec=duration_sec,
            summary_bullets=args.summary if args.summary else [args.topic]
        )

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"[+] Successfully generated structured transcript at: {output_path}")

    finally:
        if os.path.exists(temp_wav):
            try:
                os.remove(temp_wav)
                print(f"[*] Cleaned up temporary audio scratch file: {temp_wav}")
            except OSError as e:
                print(f"[!] Warning: could not remove temporary file {temp_wav}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
