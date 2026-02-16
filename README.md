# ENOLC – Domain Homoglyph Finder

ENOLC is a command‑line tool that generates homoglyph (look‑alike) variants for a given domain name, helping you analyze potential spoofed domains for phishing and brand impersonation. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)

## Features

- Generates Unicode homoglyph variants for Latin domain names using Cyrillic and Greek confusable characters.(https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
- Only mutates the label (e.g., `facebook` in `facebook.com`), preserving the original TLD.(https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
- Prints a nicely formatted table to the console showing each spoof position and variant.(https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
- Saves the results to a per‑domain `_homoglyphs.txt` file in the same directory as the script. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
- Supports both CLI arguments and interactive prompt input. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)

## How It Works

- A `CONFUSABLES` mapping defines which non‑Latin homoglyphs are available for each Latin character (e.g. `a -> а, α`, `o -> о, ο, О`). (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
- The script splits the input into `<name>` and `<tld>` parts (e.g. `facebook.com` → `facebook` + `.com`) and only generates variants for `<name>`. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
- For every character position in `<name>`, ENOLC replaces that character with each of its configured homoglyphs, skipping identical code points and case‑insensitive duplicates. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
- Each variant is rendered in a table row with:
  - `Pos`: zero‑based index in the name  
  - `Orig`: original character  
  - `Spoof`: homoglyph character  
  - `Original`: original domain with the focused character wrapped in `[...]`  
  - `Variant`: spoofed domain with the homoglyph wrapped in `[...]` (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
- Output lines are written both to stdout and to a file named `<sanitized-domain>_homoglyphs.txt` (for example, `facebook.com_homoglyphs.txt`). (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)

## Installation

No external dependencies are required beyond the Python standard library. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)

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

- Print an ASCII banner and the homoglyph table to your terminal. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
- Create `facebook.com_homoglyphs.txt` in the same directory as `enolc_V1.py`. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)

### Interactive mode

Run the script without arguments to be prompted:

```bash
python3 enolc_V1.py
```

Then enter a domain when prompted:

```text
Domain: facebook.com
```

- Press `Ctrl+C` to exit gracefully (“Exiting.”). (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
- If you submit an empty string, the script exits with “No domain provided. Exiting.” (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)

### Input normalization and output file naming

Before creating the output file, the script normalizes the domain string:(https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)

- Strips leading `http://` or `https://`.  
- Trims leading/trailing slashes and lowercases the value.  
- Replaces any character not matching `[a-z0-9._-]` with `_`.  

The result is used as the base of `<domain>_homoglyphs.txt` inside the script directory.(https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)

## Example

For an input of `facebook.com`, a portion of the output table may look similar to:

```text
Pos | Orig | Spoof | Original        | Variant
----+------+-------+-----------------+-----------------
0   | f    | ...   | [f]acebook.com  | [<homoglyph>]acebook.com
...
```

Each row highlights the character in its position for both the original and homoglyph variant to make visual comparison easier. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)

## Project Structure

- `enolc_V1.py` – Main script implementing:
  - `CONFUSABLES` homoglyph mapping. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
  - Helper functions: `script_dir`, `safe_filename`, `split_domain`. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
  - Core generator: `generate_lookalikes(domain)`. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
  - CLI entry point guarded by `if __name__ == "__main__":`. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)

## Disclaimer

The script banner includes a disclaimer stating that ENOLC is for educational and research purposes only. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
Use this tool responsibly and only on domains you are authorized to test. (https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/93916732/65f3fb13-dab6-4c6a-8d3b-0135ad49e6c9/enolc_V1.py)
