import os
import re
from pathlib import Path
from pdfminer.high_level import extract_text

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT
OUT_DIR = ROOT / "extracted"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Extract only first N pages to capture title/abstract/intro efficiently.
PAGES = 3

pdfs = sorted([p for p in PDF_DIR.iterdir() if p.suffix.lower() == '.pdf'])

for pdf in pdfs:
    out = OUT_DIR / (pdf.stem + ".txt")
    try:
        text = extract_text(str(pdf), page_numbers=list(range(PAGES))) or ""
    except Exception as e:
        out.write_text(f"[EXTRACTION_ERROR] {e}\n", encoding="utf-8")
        continue

    # Normalize whitespace a bit (keep newlines but collapse excessive spaces)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    # Guard against enormous dumps (some PDFs repeat headers); cap to ~80k chars.
    if len(text) > 80000:
        text = text[:80000] + "\n\n[TRUNCATED]\n"

    out.write_text(text, encoding="utf-8")

print(f"Extracted {len(pdfs)} PDFs -> {OUT_DIR}")
