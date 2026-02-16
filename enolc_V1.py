#!/usr/bin/env python3
"""
Domain Homoglyph Finder – ENOLC Edition

- Input: domain (CLI arg or prompt)
- Output:
    * Console: banner + table of homoglyph variants
    * File: <domain>_homoglyphs.txt saved next to this script
"""

import sys
import os
import re

# ---------------- Banner ---------------- #

BANNER = r"""
                      __          
                     (_ )        
   __    ___     _    | |    ___ 
 /'__`\/' _ `\ /'_`\  | |  /'___)
(  ___/| ( ) |( (_) ) | | ( (___ 
`\____)(_) (_)`\___/'(___)`\____)

 [ ENOLC ]

 Author   : rootadbc
 LinkedIn : linkedin.com/in/rootadbc
----------------------------------------------------
 Disclaimer: For educational and research purposes only.
----------------------------------------------------
"""

# ------------- Confusable mappings: Latin -> non‑Latin ------------- #

CONFUSABLES = {
    'a': ['а', 'α'],
    'b': ['Ь', 'В'],
    'c': ['с'],
    'e': ['е', 'ε'],
    'g': ['г'],
    'h': ['һ', 'Н'],
    'i': ['і', 'ι'],
    'k': ['к', 'κ', 'К'],
    'l': ['ӏ', 'λ'],
    'm': ['м', 'Μ'],
    'n': ['ո', 'Ν'],
    'o': ['о', 'ο', 'О'],
    'p': ['р', 'ρ', 'Р'],
    's': ['ѕ', 'Ѕ'],
    't': ['т', 'Τ', 'Τ'],
    'u': ['υ'],
    'v': ['ν', 'ѵ'],
    'x': ['х', 'Χ'],
    'y': ['у', 'Υ'],
    'A': ['А', 'Α'],
    'B': ['В', 'Β'],
    'C': ['С'],
    'E': ['Е', 'Ε'],
    'H': ['Н', 'Η'],
    'I': ['І', 'Ι'],
    'K': ['К', 'Κ'],
    'M': ['М', 'Μ'],
    'N': ['Ν'],
    'O': ['О', 'Ο'],
    'P': ['Р', 'Ρ'],
    'S': ['Ѕ'],
    'T': ['Т', 'Τ'],
    'U': ['Ս', 'Υ'],
    'X': ['Х', 'Χ'],
    'Y': ['Υ'],
}

# ---------------- Helpers ---------------- #

def script_dir() -> str:
    """Directory where this script lives."""
    return os.path.dirname(os.path.abspath(__file__))

def safe_filename(domain: str) -> str:
    """Return full path to per-domain result file in script folder."""
    domain = re.sub(r'^https?://', '', domain.strip(), flags=re.IGNORECASE)
    domain = domain.strip('/').lower()
    domain = re.sub(r'[^a-z0-9._-]+', '_', domain)
    return os.path.join(script_dir(), f"{domain}_homoglyphs.txt")

def split_domain(domain: str):
    """
    Split 'facebook.com' -> ('facebook', '.com')
    If there is no dot, returns (domain, '').
    """
    domain = domain.strip()
    if '.' not in domain:
        return domain, ''
    name, tld = domain.rsplit('.', 1)
    return name, '.' + tld

# ---------------- Core ---------------- #

def generate_lookalikes(domain: str):
    """Generate homoglyph variants, print table, save to file."""
    print(BANNER)

    original_full = domain.strip()
    name, tld = split_domain(original_full)  # only mutate name part
    chars = list(name)

    # rows: (pos, orig_char, spoof_char, original_display, variant_display)
    rows = []

    for i, ch in enumerate(chars):
        alts = CONFUSABLES.get(ch, [])
        for alt in alts:
            # skip identical letters
            if alt == ch:
                continue
            if alt.lower() == ch.lower():
                continue

            # spoofed name (plain)
            new_chars = chars[:]
            new_chars[i] = alt

            # ORIGINAL with [orig] at same index (name only)
            orig_disp_chars = []
            for j, c in enumerate(chars):
                if j == i:
                    orig_disp_chars.append(f"[{c}]")
                else:
                    orig_disp_chars.append(c)
            original_display = ''.join(orig_disp_chars) + tld

            # VARIANT with [spoof] at same index (name only)
            var_disp_chars = []
            for j, c in enumerate(new_chars):
                if j == i:
                    var_disp_chars.append(f"[{c}]")
                else:
                    var_disp_chars.append(c)
            variant_display = ''.join(var_disp_chars) + tld

            rows.append((str(i), ch, alt, original_display, variant_display))

    # Build console/file lines
    lines = [f"Domain: {original_full}"]

    if not rows:
        lines.append("")
        lines.append("No homoglyph variants for this domain.")
    else:
        headers = ("Pos", "Orig", "Spoof", "Original", "Variant")
        data_rows = []

        for pos, orig_char, spoof_char, original_display, variant_display in rows:
            data_rows.append((pos, orig_char, spoof_char, original_display, variant_display))

        # column widths
        col_widths = [len(h) for h in headers]
        for r in data_rows:
            for idx, cell in enumerate(r):
                col_widths[idx] = max(col_widths[idx], len(cell))

        def fmt_row(cells):
            return " | ".join(cells[i].ljust(col_widths[i]) for i in range(len(cells)))

        sep = "-+-".join("-" * w for w in col_widths)

        lines.append("")
        lines.append(fmt_row(headers))
        lines.append(sep)
        for r in data_rows:
            lines.append(fmt_row(r))

    # Print to console
    print()
    for line in lines:
        print(line)

    # Save to file
    out_path = safe_filename(original_full)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\nSaved to: {out_path}\n")

# ---------------- Entry point ---------------- #

if __name__ == "__main__":
    if len(sys.argv) > 1:
        domain = " ".join(sys.argv[1:])
    else:
        try:
            domain = input("Domain: ").strip()
        except KeyboardInterrupt:
            print("\nExiting.")
            sys.exit(0)

    if not domain:
        print("No domain provided. Exiting.")
        sys.exit(0)

    generate_lookalikes(domain)
