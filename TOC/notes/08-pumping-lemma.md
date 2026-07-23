# 🎈 Lesson 8 — The Pumping Lemma

> **TL;DR**: The Pumping Lemma is a mathematical trick used to prove that a language is **NOT** regular. You *cannot* use it to prove a language is regular. Just memorize these 10 steps and you'll nail the proof questions on the exam!

---

## 🛠️ The 10-Step Proof Template

When the exam asks you to prove that a language (like $L = \{a^n b^n \mid n \ge 0\}$) is **not regular**, just copy-paste these exact 10 steps into your answer and fill in the blanks:

1. **Assume the opposite**: "We assume that $L$ is regular."
2. **State the Lemma**: "So, the pumping lemma should hold for $L$."
3. **Define a length**: "It has to have a pumping length (let's call it $P$)."
4. **State the condition**: "All strings in $L$ longer than $P$ can be pumped ($|w| \ge P$)."
5. **Pick a string**: "Now find a string $w$ in $L$ such that $|w| \ge P$." *(Example: Let $w = a^P b^P$)*
6. **Divide the string**: "Divide $w$ into 3 parts: $x$, $y$, and $z$ ($w = xyz$)."
7. **Pump it up**: "Show that $x y^i z \notin L$ for some $i$." *(Usually we pick $i = 2$ to "pump" it up, or $i = 0$ to pump it down).*
8. **Check combinations**: "Then consider all ways that $w$ can be divided into $x$, $y$, and $z$."
9. **Break the rules**: "Show that none of these divisions can satisfy all 3 pumping conditions at the same time."
10. **Conclusion**: "$w$ cannot be pumped = **CONTRADICTION**. Therefore, $L$ is not regular." ✅

---

## 🛑 What are the "3 Pumping Conditions"?
If you're asked for the actual conditions that must be broken (mentioned in Step 9), they are:
1. $xy^iz \in L$ for all $i \ge 0$
2. $|y| > 0$ (the part we pump isn't empty)
3. $|xy| \le P$ (the part we pump is near the beginning)

> **💡 Exam Tip**: You literally just need to memorize the 10 steps. Most professors just want to see the sequence of logic!
