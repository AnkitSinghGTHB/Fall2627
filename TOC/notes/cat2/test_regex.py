import re

s = r"First terminal generated = FIRST; symbol immediately to right = FOLLOW. Add $\$$ to $\text{FOLLOW}(S)$."

# 1. Protect escaped dollars
s_clean = s.replace(r"\$", "ESCDOLLAR_PLACEHOLDER")

# 2. Match display math
display_matches = re.findall(r"\$\$(.*?)\$\$", s_clean, flags=re.DOTALL)
print("Display matches:", display_matches)

# 3. Match inline math
inline_matches = re.findall(r"\$([^\$\n]+?)\$", s_clean)
print("Inline matches:", [m.replace("ESCDOLLAR_PLACEHOLDER", r"\$") for m in inline_matches])
