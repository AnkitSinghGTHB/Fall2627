import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\ankit\Fall2627\Python\notes\cat2"
md_path = os.path.join(BASE_DIR, "PYTHON_CAT2_FOOLPROOF_SOLVE_BOOKLET.md")

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect blockquotes
print("Original characters:", len(text))
print("Original lines:", len(text.splitlines()))

# 1. Replace verbose blockquote headers
# "> ### 📋 Target Exam Question / Problem Statement:" -> "> 📋 **Exam Problem Statement:**"
text = re.sub(
    r">\s*###\s*📋\s*Target Exam Question / Problem Statement:\s*\n",
    r"> 📋 **Exam Problem:** ",
    text
)

# 2. Compact code blocks:
# We process each ```python ... ``` block
def compact_python_code(match):
    code = match.group(1)
    lines = code.splitlines()
    new_lines = []
    pending_comment = None

    for line in lines:
        stripped = line.strip()
        
        # Skip pure decorative separator lines
        if re.match(r"^#\s*[-=]{5,}", stripped):
            continue
        
        # If line is a comment
        if stripped.startswith("#"):
            comment_text = stripped.lstrip("#").strip()
            # If we don't have a pending comment, save it
            if not pending_comment:
                pending_comment = comment_text
            else:
                pending_comment += "; " + comment_text
            continue

        # If line is empty
        if not stripped:
            if pending_comment:
                # keep comment on its own line if followed by blank
                new_lines.append(f"# {pending_comment}")
                pending_comment = None
            if new_lines and new_lines[-1] != "":
                new_lines.append("")
            continue

        # If it's a code line and we have a pending comment
        if pending_comment:
            # Put comment on the right side if line isn't too long
            indent = len(line) - len(line.lstrip())
            indent_str = " " * indent
            clean_code = line.strip()
            if len(line) + len(pending_comment) < 110:
                new_lines.append(f"{line}  # {pending_comment}")
            else:
                new_lines.append(f"{indent_str}# {pending_comment}")
                new_lines.append(line)
            pending_comment = None
        else:
            new_lines.append(line)

    if pending_comment:
        new_lines.append(f"# {pending_comment}")

    # Remove consecutive blank lines
    final_lines = []
    for l in new_lines:
        if l == "" and final_lines and final_lines[-1] == "":
            continue
        final_lines.append(l)

    return "```python\n" + "\n".join(final_lines) + "\n```"

compacted_text = re.sub(r"```python(.*?)```", compact_python_code, text, flags=re.DOTALL)

# Also compact output blocks: remove unnecessary blank lines
def compact_output(match):
    out = match.group(1)
    lines = [l for l in out.splitlines() if l.strip() != ""]
    return "```text\n" + "\n".join(lines) + "\n```"

compacted_text = re.sub(r"```text(.*?)```", compact_output, compacted_text, flags=re.DOTALL)

# Reduce multiple blank lines in markdown to at most 1
compacted_text = re.sub(r"\n{3,}", "\n\n", compacted_text)

print("Compacted characters:", len(compacted_text))
print("Compacted lines:", len(compacted_text.splitlines()))

compact_md_path = os.path.join(BASE_DIR, "PYTHON_CAT2_FOOLPROOF_SOLVE_BOOKLET_COMPACT.md")
with open(compact_md_path, "w", encoding="utf-8") as f:
    f.write(compacted_text)

print("Saved test compacted file:", compact_md_path)
