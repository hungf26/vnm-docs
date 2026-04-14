"""
Split pandoc-converted Markdown into separate MkDocs pages.
Run: python split_docs.py
"""
import re
import os

INPUT = "full-converted.md"
DOCS = "docs"

# ── helpers ───────────────────────────────────────────────────────────────────

def clean(text: str) -> str:
    """General cleanup of pandoc artifacts."""
    # Remove pandoc anchor IDs like {#_section_name}
    text = re.sub(r'\s*\{#[^}]+\}', '', text)
    # Remove image size attributes {height="..." width="..."}
    text = re.sub(r'\{[^}]*(?:height|width)[^}]*\}', '', text)
    # Remove bold from headings  (**text** → text)
    text = re.sub(r'^(#{1,6})\s+\*\*(.+?)\*\*', r'\1 \2', text, flags=re.MULTILINE)
    # Fix bullet points using • or ∙
    text = re.sub(r'^[•∙]\s+', '- ', text, flags=re.MULTILINE)
    # Remove leftover backslash line-continuations from adoc (+)
    text = re.sub(r'\\\n', '\n', text)
    # Fix adoc passthrough ++text++ → `text`
    text = re.sub(r'\+\+([^+]+)\+\+', r'`\1`', text)
    # Fix {plus} → +
    text = text.replace('{plus}', '+')
    # Fix ++ lone → remove
    text = re.sub(r'\+\+\s*\+\+', '', text)
    # Clean up excessive blank lines (max 2)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'


def write(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(clean(content))
    print(f"  wrote {path}")


# ── load full file ─────────────────────────────────────────────────────────────

with open(INPUT, encoding='utf-8') as f:
    raw = f.read()

# Split on H2 sections (## **N. Title** or ## **Title**)
# We'll use a marker approach: find all H1 and H2 positions

lines = raw.split('\n')

# Build a list of (line_index, level, title, raw_title_line)
sections = []  # (line_index, level, heading_text)
for i, line in enumerate(lines):
    m1 = re.match(r'^# \*\*(.+?)\*\*', line)
    m2 = re.match(r'^## \*\*(.+?)\*\*', line)
    m3 = re.match(r'^# (.+)', line)
    m2b = re.match(r'^## (.+)', line)
    if m1:
        sections.append((i, 1, m1.group(1).strip()))
    elif m2:
        sections.append((i, 2, m2.group(1).strip()))
    elif m3 and not m1:
        sections.append((i, 1, m3.group(1).strip()))
    elif m2b and not m2:
        sections.append((i, 2, m2b.group(1).strip()))

def get_block(start_idx, end_idx):
    return '\n'.join(lines[start_idx:end_idx])

# Find chapter boundaries
chap_indices = [(i, idx) for i, (idx, lvl, _) in enumerate(sections) if lvl == 1]

# ── Chapter I: Overview (H1 index 0) ──────────────────────────────────────────
# Sections: 1.Intro 2.Overview 3.Interface 4.Requirements 5.Installation

# Map H2 section names to output files
OVERVIEW_MAP = {
    '1': ('overview/introduction.md',      '# Introduction'),
    '2': ('overview/simcenter-overview.md', '# VNM SimCenter Overview'),
    '3': ('overview/software-interface.md', '# Software Interface'),
    '4': ('overview/system-requirements.md','# System Requirements'),
    '5': ('overview/installation.md',       '# Software Installation'),
}

HARDWARE_MAP = {
    '1': ('hardware/safety.md',           '# Safety Notice'),
    '2': ('hardware/usb-connection.md',   '# USB Connection'),
    '3': ('hardware/power-connection.md', '# Power Connection'),
    '4': ('hardware/mounting.md',         '# Mounting the Wheelbase'),
    '5': ('hardware/steering-wheel.md',   '# Attaching the Steering Wheel'),
    '6': ('hardware/additional-devices.md','# Connecting Additional Devices'),
    '7': ('hardware/power-on.md',         '# Power-On Procedure'),
    '8': ('hardware/device-detection.md', '# Verify Device Detection'),
}

WHEELBASE_MAP = {
    '1': ('wheelbase/index.md',              '# Wheelbase Configuration — Overview'),
    '2': ('wheelbase/basic-settings.md',     '# Basic Settings'),
    '3': ('wheelbase/advanced-settings.md',  '# Advanced Settings'),
    '4': ('wheelbase/game-settings.md',      '# Game Settings'),
    '5': ('wheelbase/profiles.md',           '# Wheelbase Profiles'),
    '6': ('wheelbase/telemetry.md',          '# Telemetry'),
    '7': ('wheelbase/telemetry-profiles.md', '# Telemetry Profiles'),
    '8': ('wheelbase/firmware.md',           '# Firmware Update'),
    '9': ('wheelbase/troubleshooting.md',    '# Troubleshooting'),
}

def extract_chapter_sections(chapter_h1_line, next_chapter_h1_line, section_map):
    """Given line boundaries for a chapter, split its H2 subsections."""
    chapter_lines = lines[chapter_h1_line:next_chapter_h1_line]

    # Find H2 positions within chapter
    h2_positions = []
    for i, line in enumerate(chapter_lines):
        m = re.match(r'^## ', line)
        if m:
            h2_positions.append(i)

    h2_positions.append(len(chapter_lines))  # sentinel

    # Extract the H1 intro text (before first H2)
    intro_text = '\n'.join(chapter_lines[1:h2_positions[0]])

    # For each H2 block
    for k in range(len(h2_positions) - 1):
        start = h2_positions[k]
        end   = h2_positions[k + 1]
        block = '\n'.join(chapter_lines[start:end])

        # Get the section number from the heading
        heading_line = chapter_lines[start]
        m = re.match(r'^## \*?\*?(\d+)\.', heading_line)
        if not m:
            m = re.match(r'^## (\d+)\.', heading_line)
        if not m:
            continue
        num = m.group(1)

        if num in section_map:
            outfile, h1_override = section_map[num]
            # Replace the H2 heading with H1
            block = re.sub(r'^## [^\n]+', h1_override, block, count=1)
            # Demote all remaining headings: H3→H2, H4→H3, H5→H4
            block = re.sub(r'^#### ', '### ', block, flags=re.MULTILINE)
            block = re.sub(r'^##### ', '#### ', block, flags=re.MULTILINE)
            block = re.sub(r'^### ', '## ', block, flags=re.MULTILINE)
            write(os.path.join(DOCS, outfile), block)

    return intro_text


# ── Find chapter start lines ────────────────────────────────────────────────────
chap_lines = {}
for i, line in enumerate(lines):
    if re.match(r'^# \*\*I\. Overview\*\*', line) or re.match(r'^# \*\*I\.', line):
        chap_lines['I'] = i
    elif re.match(r'^# \*\*II\. Hardware', line) or re.match(r'^# \*\*II\.', line):
        chap_lines['II'] = i
    elif re.match(r'^# \*\*III\. Wheelbase', line) or re.match(r'^# \*\*III\.', line):
        chap_lines['III'] = i

print("Chapter boundaries found:", chap_lines)

if 'I' in chap_lines and 'II' in chap_lines and 'III' in chap_lines:
    print("\nProcessing Overview (Chapter I)...")
    extract_chapter_sections(chap_lines['I'], chap_lines['II'], OVERVIEW_MAP)

    print("\nProcessing Hardware Setup (Chapter II)...")
    extract_chapter_sections(chap_lines['II'], chap_lines['III'], HARDWARE_MAP)

    print("\nProcessing Wheelbase Configuration (Chapter III)...")
    extract_chapter_sections(chap_lines['III'], len(lines), WHEELBASE_MAP)

    print("\nAll files written successfully!")
else:
    print("ERROR: Could not find chapter boundaries. Found:", chap_lines)
    print("First 20 H1/H2 headings:")
    for i, line in enumerate(lines[:200]):
        if line.startswith('#'):
            print(f"  line {i}: {line[:80]}")
