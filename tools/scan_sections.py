import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "deep_extracted"

# Common section markers (very heuristic across venues)
SECTION_PATTERNS = {
    "abstract": re.compile(r"^\s*abstract\b", re.IGNORECASE),
    "introduction": re.compile(r"^\s*\d+\s*\.\s*introduction\b|^\s*introduction\b", re.IGNORECASE),
    "related_work": re.compile(r"^\s*\d+\s*\.\s*related work\b|^\s*related work\b", re.IGNORECASE),
    "method": re.compile(r"^\s*\d+\s*\.\s*(method|methodology|approach)\b|^\s*(method|methodology|approach)\b", re.IGNORECASE),
    "data": re.compile(r"^\s*\d+\s*\.\s*(data|dataset|datasets)\b|^\s*(data|dataset|datasets)\b", re.IGNORECASE),
    "experiments": re.compile(r"^\s*\d+\s*\.\s*experiments\b|^\s*experiments\b", re.IGNORECASE),
    "results": re.compile(r"^\s*\d+\s*\.\s*results\b|^\s*results\b", re.IGNORECASE),
    "evaluation": re.compile(r"^\s*\d+\s*\.\s*evaluation\b|^\s*evaluation\b", re.IGNORECASE),
    "discussion": re.compile(r"^\s*\d+\s*\.\s*discussion\b|^\s*discussion\b", re.IGNORECASE),
    "limitations": re.compile(r"^\s*\d+\s*\.\s*limitations\b|^\s*limitations\b", re.IGNORECASE),
    "conclusion": re.compile(r"^\s*\d+\s*\.\s*conclusion\b|^\s*conclusions\b|^\s*conclusion\b", re.IGNORECASE),
}

# Fallback: search anywhere in a line for weaker markers
WEAK_MARKERS = {
    "conclusion": re.compile(r"\bconclusion(s)?\b", re.IGNORECASE),
    "limitations": re.compile(r"\blimitation(s)?\b", re.IGNORECASE),
    "experiments": re.compile(r"\bexperiment(s)?\b", re.IGNORECASE),
    "results": re.compile(r"\bresults\b", re.IGNORECASE),
}

out = {}

for path in sorted(DIR.glob('*.txt')):
    lines = path.read_text(encoding='utf-8', errors='replace').splitlines()
    hits = {}

    # Strong heading-like matches
    for i, line in enumerate(lines, start=1):
        for name, pat in SECTION_PATTERNS.items():
            if name in hits:
                continue
            if pat.search(line.strip()):
                hits[name] = i

    # Weak fallbacks if missing
    for name, pat in WEAK_MARKERS.items():
        if name in hits:
            continue
        for i, line in enumerate(lines, start=1):
            if pat.search(line):
                hits[name] = i
                break

    out[path.name] = {
        "n_lines": len(lines),
        "hits": hits,
    }

print(json.dumps(out, indent=2, sort_keys=True))
