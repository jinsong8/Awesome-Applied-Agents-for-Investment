import re
from pathlib import Path
from pdfminer.high_level import extract_text

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "deep_extracted"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Folders to include (non-survey)
IN_DIRS = [
    ROOT / "01_Agentic_Trading_and_Strategy_Automation",
    ROOT / "02_Text_Signals_from_News_Calls_Filings",
    ROOT / "03_Risk_Crash_and_Volatility",
    ROOT / "05_Benchmarks_and_Datasets",
    ROOT / "04_IE_and_Interpretable_Text_Methods",
]

# Heuristic patterns that often mark the start of appendices/supplement.
APPENDIX_PATTERNS = [
    r"\n\s*appendix\s+[a-z0-9]+\b",
    r"\n\s*appendix\b",
    r"\n\s*appendices\b",
    r"\n\s*online\s+appendix\b",
    r"\n\s*supplementary\s+material\b",
    r"\n\s*supplement\b",
    r"\n\s*additional\s+results\b",
    r"\n\s*extra\s+experiments\b",
    r"\n\s*ablation\s+details\b",
]
APPENDIX_RE = re.compile("|".join(APPENDIX_PATTERNS), re.IGNORECASE)

# Cap to avoid runaway size (some PDFs duplicate headers); still enough for full paper.
MAX_CHARS = 1_200_000

pdfs = []
for d in IN_DIRS:
    pdfs.extend(sorted(d.glob("*.pdf")))

for pdf in pdfs:
    out = OUT_DIR / (pdf.stem + ".txt")
    try:
        text = extract_text(str(pdf)) or ""
    except Exception as e:
        out.write_text(f"[EXTRACTION_ERROR] {e}\n", encoding="utf-8")
        continue

    # Normalize whitespace lightly
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    # Truncate at appendix if found (we keep the main body only)
    m = APPENDIX_RE.search(text)
    if m:
        text = text[: m.start()] + "\n\n[TRUNCATED_BEFORE_APPENDIX]\n"

    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS] + "\n\n[TRUNCATED_MAX_CHARS]\n"

    out.write_text(text, encoding="utf-8")

print(f"Extracted {len(pdfs)} PDFs -> {OUT_DIR}")
