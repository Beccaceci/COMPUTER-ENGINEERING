#!/usr/bin/env python3
"""
verify_coverage.py - Concept Coverage & Style Auditor for Sicurezza dei Sistemi Informativi
Audits study guide LaTeX files against extracted lecture concepts, official dispense topics, and exam questions.
Optionally verifies adherence to the direct academic style of the official notes (no third-person meta-commentary).
"""

import sys
import argparse
import re
from pathlib import Path

PROHIBITED_STYLE_PATTERNS = [
    (r"\b(professore\s+basile|prof\.\s*basile)\b", "Attributing statements directly to the professor (use direct authoritative voice)"),
    (r"\b(come\s+detto\s+a\s+lezione|spiegato\s+a\s+lezione|durante\s+la\s+lezione)\b", "Oral lecture meta-reference (state concepts directly)"),
    (r"\b(nella\s+slide|nelle\s+slide|dalla\s+slide|vedere\s+slide)\b", "Slide deck reference (study guide must be self-contained)"),
    (r"\b(il\s+presente\s+capitolo\s+si\s+propone\s+di)\b", "Generic chapter meta-introduction (begin immediately with technical content)")
]

def audit_coverage(tex_file: Path, required_keywords: list[str]) -> bool:
    if not tex_file.exists():
        print(f"[ERROR] Target TeX file not found: {tex_file}", file=sys.stderr)
        return False
    
    content = tex_file.read_text(encoding="utf-8")
    missing = []
    
    for kw in required_keywords:
        pattern = re.compile(rf"\b{re.escape(kw)}\b", re.IGNORECASE)
        if not pattern.search(content):
            missing.append(kw)
            
    if missing:
        print(f"[FAIL] {tex_file.name} is missing {len(missing)} mandatory concepts:")
        for m in missing:
            print(f"  - {m}")
        return False
        
    print(f"[PASS] {tex_file.name} covers all {len(required_keywords)} checked concepts.")
    return True

def audit_style(tex_file: Path) -> bool:
    if not tex_file.exists():
        return False
        
    content = tex_file.read_text(encoding="utf-8")
    lines = content.splitlines()
    violations = []
    
    for line_idx, line in enumerate(lines, 1):
        # Ignore comments
        stripped = line.strip()
        if stripped.startswith("%"):
            continue
            
        for pattern_str, reason in PROHIBITED_STYLE_PATTERNS:
            match = re.search(pattern_str, line, re.IGNORECASE)
            if match:
                violations.append((line_idx, match.group(0), reason, line.strip()))
                
    if violations:
        print(f"[WARN] Found {len(violations)} style rule violations in {tex_file.name}:")
        for line_num, matched_text, reason, text in violations:
            print(f"  Line {line_num}: Found '{matched_text}' -> {reason}")
            print(f"    Text: {text[:100]}")
        return False
        
    print(f"[PASS] {tex_file.name} adheres cleanly to official dispensa style guidelines.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Audit study guide concept coverage and style compliance.")
    parser.add_argument("--tex-file", required=True, type=Path, help="Path to chapter .tex file")
    parser.add_argument("--keywords-file", required=False, type=Path, help="File containing newline-separated keywords")
    parser.add_argument("--check-style", action="store_true", help="Perform style linting against prohibited meta-commentary")
    args = parser.parse_args()
    
    all_ok = True
    
    if args.keywords_file:
        keywords = [line.strip() for line in args.keywords_file.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")]
        if not audit_coverage(args.tex_file, keywords):
            all_ok = False
            
    if args.check_style:
        if not audit_style(args.tex_file):
            all_ok = False
            
    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()
