"""
Build VNM Direct Drive User Manual pages for MkDocs.
Run from vnm-docs/ folder: python build_user_manual.py
"""
import re, os, zipfile, shutil

DOCX   = "VNM Direct Drive User Manual.docx"
INPUT  = "user-manual-converted.md"
DOCS   = "docs/user-manual"
IMGDIR = f"{DOCS}/media"

os.makedirs(IMGDIR, exist_ok=True)

# ── 1. Extract images from docx ──────────────────────────────────────────────
print("Extracting images from docx...")
with zipfile.ZipFile(DOCX) as z:
    imgs = [f for f in z.namelist() if f.startswith("word/media/")]
    for src in sorted(imgs):
        name = os.path.basename(src)
        dst  = f"{IMGDIR}/{name}"
        with z.open(src) as fin, open(dst, "wb") as fout:
            fout.write(fin.read())
        print(f"  {name}")

# ── 2. Load converted markdown ────────────────────────────────────────────────
with open(INPUT, encoding="utf-8") as f:
    raw = f.read()

def clean(text: str) -> str:
    # Remove pandoc anchor IDs {#_...}
    text = re.sub(r'\s*\{#[^}]+\}', '', text)
    # Remove image size attrs {height="..." width="..."}
    text = re.sub(r'\{[^}]*(?:height|width)[^}]*\}', '', text)
    # Remove bold from headings
    text = re.sub(r'^(#{1,6})\s+\*\*(.+?)\*\*\s*$', r'\1 \2', text, flags=re.MULTILINE)
    # Clean up excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(clean(content))
    print(f"  wrote {path}")

# ── 3. Split by H1 sections ───────────────────────────────────────────────────
lines = raw.split('\n')

# Find H1 positions (skip the "Contents" one)
sections = []
for i, line in enumerate(lines):
    m = re.match(r'^# \*\*(\d+)\. (.+?)\*\*', line)
    if m:
        sections.append((i, m.group(1), m.group(2).strip()))

sections.append((len(lines), None, None))  # sentinel
print(f"\nFound {len(sections)-1} sections:")
for i, num, title in sections[:-1]:
    print(f"  {num}. {title} (line {i})")

def get_section(s_idx):
    start, end = sections[s_idx][0], sections[s_idx+1][0]
    return '\n'.join(lines[start:end])

# ── 4. Write pages ────────────────────────────────────────────────────────────
print("\nWriting pages...")

# index.md — home + specifications (section 1)
sec1 = get_section(0)
# Replace H1 heading
sec1 = re.sub(r'^# \*\*1\. VNM Direct Drive Wheelbase specifications\*\*',
              '# VNM Direct Drive Wheelbase Specifications', sec1)
write(f"{DOCS}/index.md", sec1)

# mounting.md — section 2
sec2 = get_section(1)
sec2 = re.sub(r'^# \*\*2\. Wheelbase Mounting Pattern\*\*',
              '# Wheelbase Mounting Pattern', sec2)
# H2 → keep as H2 (already correct level)
write(f"{DOCS}/mounting.md", sec2)

# connection.md — section 3
sec3 = get_section(2)
sec3 = re.sub(r'^# \*\*3\. Connection\*\*', '# Connection', sec3)
write(f"{DOCS}/connection.md", sec3)

# safety.md — sections 4 + 5 combined
sec4 = get_section(3)
sec5 = get_section(4)
sec4 = re.sub(r'^# \*\*4\. Product safety warnings and instructions\*\*',
              '# Safety Warnings & Instructions', sec4)
sec5 = re.sub(r'^# \*\*5\. Safe Operation instruction\*\*',
              '## Safe Operation Instructions', sec5)
# Demote H2 in sec5 to H3
sec5 = re.sub(r'^## ', '### ', sec5, flags=re.MULTILINE)
combined = sec4.rstrip() + "\n\n" + sec5
write(f"{DOCS}/safety.md", combined)

print("\nAll user manual pages written!")
print(f"Images → {IMGDIR}/")
