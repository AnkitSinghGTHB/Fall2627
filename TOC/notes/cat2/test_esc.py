import re

text = r"Here is $\text{FOLLOW}(S) = \{\$\}$ in math and another $x + y$."
pattern = r'(?<!\\)\$((?:\\\$|[^$\n])+?)(?<!\\)\$'
matches = list(re.finditer(pattern, text))
print("Total matches:", len(matches))
for m in matches:
    print("  Matched:", m.group(0))
    print("  Inside :", m.group(1))
