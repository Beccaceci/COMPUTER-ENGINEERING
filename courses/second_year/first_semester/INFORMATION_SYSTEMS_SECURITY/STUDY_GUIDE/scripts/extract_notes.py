#!/usr/bin/env python3
"""
extract_notes.py - Automated Dispensa Ingestion Utility
Extracts text, table of contents, and section structures from the professor's official notes PDF.
Used in Phase 1 of the lecture-study-guide-integrator workflow.
"""

import sys
import argparse
import json
import re
from pathlib import Path
import pypdf

def extract_pdf_structure(pdf_path: Path) -> dict:
    if not pdf_path.exists():
        raise FileNotFoundError(f"Notes PDF not found: {pdf_path}")
        
    reader = pypdf.PdfReader(str(pdf_path))
    num_pages = len(reader.pages)
    
    pages_text = []
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages_text.append({
            "page_num": idx + 1,
            "text": text
        })
        
    full_text = "\n\n".join([f"=== PAGE {p['page_num']} ===\n{p['text']}" for p in pages_text])
    
    # Simple regex extraction for sections and subsections
    headings = []
    section_pattern = re.compile(r"^(\d+\.\d+(?:\.\d+)?)\s+(.+)$", re.MULTILINE)
    for match in section_pattern.finditer(full_text):
        headings.append({
            "number": match.group(1),
            "title": match.group(2).strip()
        })
        
    return {
        "pdf_name": pdf_path.name,
        "total_pages": num_pages,
        "headings": headings,
        "full_text": full_text
    }

def main():
    parser = argparse.ArgumentParser(description="Extract structured text from official course notes PDF.")
    parser.add_argument("--pdf", required=True, type=Path, help="Path to official notes PDF")
    parser.add_argument("--output-json", type=Path, help="Optional output JSON path")
    parser.add_argument("--output-txt", type=Path, help="Optional output raw text path")
    args = parser.parse_args()
    
    data = extract_pdf_structure(args.pdf)
    print(f"[OK] Extracted {data['total_pages']} pages from {data['pdf_name']}.")
    print(f"[OK] Detected {len(data['headings'])} potential section headings.")
    
    if args.output_json:
        args.output_json.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[OK] Wrote JSON structure to {args.output_json}")
        
    if args.output_txt:
        args.output_txt.write_text(data["full_text"], encoding="utf-8")
        print(f"[OK] Wrote raw text to {args.output_txt}")

if __name__ == "__main__":
    main()
