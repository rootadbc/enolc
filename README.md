# ENOLC – Domain Homoglyph Finder

ENOLC is a command‑line tool that generates homoglyph (look‑alike) variants for a given domain name, helping you analyze potential spoofed domains for phishing and brand impersonation.

## Features

- Generates Unicode homoglyph variants for Latin domain names using Cyrillic and Greek confusable characters.
- Only mutates the label (e.g., `facebook` in `facebook.com`), preserving the original TLD.
- Prints a nicely formatted table to the console showing each spoof position and variant.
- Saves the results to a per‑domain `_homoglyphs.txt` file in the same directory as the script. 
- Supports both CLI arguments and interactive prompt input. 

## How It Works

- A `CONFUSABLES` mapping defines which non‑Latin homoglyphs are available for each Latin character (e.g. `a -> а, α`, `o -> о, ο, О`). 
- The script splits the input into `<name>` and `<tld>` parts (e.g. `facebook.com` → `facebook` + `.com`) and only generates variants for `<name>`. 
- For every character position in `<name>`, ENOLC replaces that character with each of its configured homoglyphs, skipping identical code points and case‑insensitive duplicates. 
- Each variant is rendered in a table row with:
  - `Pos`: zero‑based index in the name  
  - `Orig`: original character  
  - `Spoof`: homoglyph character  
  - `Original`: original domain with the focused character wrapped in `[...]`  
  - `Variant`: spoofed domain with the homoglyph wrapped in `[...]` 
- Output lines are written both to stdout and to a file named `<sanitized-domain>_homoglyphs.txt` (for example, `facebook.com_homoglyphs.txt`). 

## Installation

No external dependencies are required beyond the Python standard library. 

- Requirements:
  - Python 3.x  
  - A terminal or shell environment  

Clone or download this repository, then ensure the script is executable:

```bash
chmod +x enolc_V1.py
```

## Usage

### Basic usage (CLI argument)

```bash
python3 enolc_V1.py facebook.com
```

This will:

- Print an ASCII banner and the homoglyph table to your terminal.
- Create `facebook.com_homoglyphs.txt` in the same directory as `enolc_V1.py`. 

### Interactive mode

Run the script without arguments to be prompted:

```bash
python3 enolc_V1.py
```

Then enter a domain when prompted:

```text
Domain: facebook.com
```

- Press `Ctrl+C` to exit gracefully (“Exiting.”). 
- If you submit an empty string, the script exits with “No domain provided. Exiting.” 

### Input normalization and output file naming

Before creating the output file, the script normalizes the domain string:

- Strips leading `http://` or `https://`.  
- Trims leading/trailing slashes and lowercases the value.  
- Replaces any character not matching `[a-z0-9._-]` with `_`.  

The result is used as the base of `<domain>_homoglyphs.txt` inside the script directory.
## Example

For an input of `facebook.com`, a portion of the output table may look similar to:

```text
Pos | Orig | Spoof | Original        | Variant
----+------+-------+-----------------+-----------------
0   | f    | ...   | [f]acebook.com  | [<homoglyph>]acebook.com
...
```

Each row highlights the character in its position for both the original and homoglyph variant to make visual comparison easier. 

## Project Structure

- `enolc_V1.py` – Main script implementing:
  - `CONFUSABLES` homoglyph mapping. 
  - Helper functions: `script_dir`, `safe_filename`, `split_domain`. 
  - Core generator: `generate_lookalikes(domain)`. 
  - CLI entry point guarded by `if __name__ == "__main__":`. 

## Disclaimer

The script banner includes a disclaimer stating that ENOLC is for educational and research purposes only. 
Use this tool responsibly and only on domains you are authorized to test. 
