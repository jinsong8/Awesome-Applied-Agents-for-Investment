import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_DIR = ROOT / 'deep_extracted'
INDEX_PATH = ROOT / 'section_index.json'
OUT_DIR = ROOT / 'reading_packets'
OUT_DIR.mkdir(parents=True, exist_ok=True)

WINDOWS = {
    'abstract': 80,
    'introduction': 220,
    'method': 260,
    'experiments': 320,
    'evaluation': 320,
    'results': 320,
    'discussion': 220,
    'limitations': 220,
    'conclusion': 220,
}

PREFERRED_MID = ['method', 'experiments', 'evaluation', 'results']

with INDEX_PATH.open('r', encoding='utf-8') as f:
    idx = json.load(f)


def clip(lines, start_1idx, n):
    # start_1idx is 1-based
    start = max(0, start_1idx - 1)
    end = min(len(lines), start + n)
    return start, end


def add_block(out_lines, title, lines, start, end):
    out_lines.append(f"### {title} (lines {start+1}-{end})")
    out_lines.append('')
    out_lines.extend(lines[start:end])
    out_lines.append('')

for name, meta in sorted(idx.items()):
    src = TEXT_DIR / name
    if not src.exists():
        continue
    lines = src.read_text(encoding='utf-8', errors='replace').splitlines()
    hits = meta.get('hits', {})

    out_lines = []
    out_lines.append(f"## Reading packet: {name}")
    out_lines.append('')
    out_lines.append(f"Source: `{src}`")
    out_lines.append('')
    out_lines.append(f"Total lines: {len(lines)}")
    out_lines.append('')

    # Always include abstract if we have it
    if 'abstract' in hits:
        s,e = clip(lines, hits['abstract'], WINDOWS['abstract'])
        add_block(out_lines, 'Abstract', lines, s, e)

    # Include intro
    if 'introduction' in hits:
        s,e = clip(lines, hits['introduction'], WINDOWS['introduction'])
        add_block(out_lines, 'Introduction', lines, s, e)

    # Include a “middle” section: method -> experiments/eval/results
    for key in PREFERRED_MID:
        if key in hits:
            s,e = clip(lines, hits[key], WINDOWS[key])
            add_block(out_lines, key.capitalize(), lines, s, e)
            break

    # Include another mid if available (often exp/results separate)
    # pick the earliest among the remaining that isn't already used
    used = set([b for b in ['method','experiments','evaluation','results'] if b in hits])
    # But we only added first one above; try add a second distinct one prioritizing results/experiments
    for key in ['results','experiments','evaluation','method']:
        if key in hits and key != (PREFERRED_MID[0] if PREFERRED_MID[0] in hits else None):
            # avoid duplicate start lines by ensuring this key differs from already included section start
            s,e = clip(lines, hits[key], WINDOWS[key])
            add_block(out_lines, key.capitalize() + ' (extra)', lines, s, e)
            break

    # Limitations and conclusion
    if 'limitations' in hits:
        s,e = clip(lines, hits['limitations'], WINDOWS['limitations'])
        add_block(out_lines, 'Limitations', lines, s, e)

    if 'conclusion' in hits:
        # include a bit before conclusion too
        s0 = max(1, hits['conclusion'] - 40)
        s,e = clip(lines, s0, WINDOWS['conclusion'] + 40)
        add_block(out_lines, 'Conclusion', lines, s, e)

    out_path = OUT_DIR / (Path(name).stem + '.md')
    out_path.write_text('\n'.join(out_lines) + '\n', encoding='utf-8')

print('wrote', len(list(OUT_DIR.glob('*.md'))), 'packets to', OUT_DIR)
