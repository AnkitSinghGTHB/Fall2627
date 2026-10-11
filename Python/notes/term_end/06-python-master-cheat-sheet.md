# 📑 CSE3011: Python Master Cheat Sheet (1-Page Rapid Reference)

> Keep this open for last-minute syntax, built-ins, and library review before the exam on October 19!

---

## 1. Core Built-In Functions & Methods
* **Collections**:
  - `list.append(x)`, `list.extend(iter)`, `list.pop(i)`, `list.sort(key=..., reverse=...)`
  - `dict.get(k, default)`, `dict.keys()`, `dict.values()`, `dict.items()`
  - `set.add(x)`, `set.union(s2)` (`|`), `set.intersection(s2)` (`&`), `set.difference(s2)` (`-`)
* **Iteration Primitives**:
  - `enumerate(iterable, start=0)`: Yields `(index, value)` pairs
  - `zip(iter1, iter2)`: Tuples combining elements in parallel
  - `map(func, iter)`, `filter(func, iter)`
* **Comprehensions**:
  - `[x**2 for x in seq if cond]` (List)
  - `{k: v for k, v in pairs}` (Dict)
  - `{x for x in seq}` (Set)

---

## 2. Dunder (Magic) Methods Reference
* **Lifecycle**: `__init__(self, ...)`, `__del__(self)`
* **Strings**: `__str__(self)` (for users), `__repr__(self)` (for developers)
* **Arithmetic**: `__add__(self, other)`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`
* **Comparison**: `__eq__(self, other)`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__`
* **Container**: `__len__(self)`, `__getitem__(self, key)`, `__setitem__(self, key, val)`

---

## 3. Regular Expressions Cheat Sheet
* `re.match(pat, s)`: Anchored at start of string
* `re.search(pat, s)`: Scans entire string
* `re.findall(pat, s)`: Returns list of all matching string instances
* `re.sub(pat, repl, s)`: String replacement
* **Tokens**: `\d` (digit), `\w` (word character), `\s` (whitespace), `^` (start), `$` (end), `+` (1+), `*` (0+), `?` (0/1)

---

## 4. File I/O & DB-API 2.0 Templates
* **File Pointer**:
  - `f.tell()`: Get current byte position
  - `f.seek(offset, whence)`: Reposition (`0=start, 1=current, 2=end`)
* **SQLite3 Workflow**:
  ```python
  import sqlite3
  conn = sqlite3.connect("db.sqlite")
  cur = conn.cursor()
  cur.execute("INSERT INTO t VALUES (?, ?)", (val1, val2))
  conn.commit()
  cur.execute("SELECT * FROM t")
  rows = cur.fetchall()
  conn.close()
  ```

---

## 5. Tkinter & Multithreading
* **Tkinter Window Lifecycle**:
  `root = tk.Tk(); root.title("App"); ...; root.mainloop()`
* **Threading with Lock**:
  ```python
  import threading
  lock = threading.Lock()
  with lock:
      # Critical section
      pass
  ```
* **TCP Socket Skeletons**:
  - Server: `s.bind((h, p)); s.listen(5); c, a = s.accept(); c.recv(1024); c.sendall(...)`
  - Client: `s.connect((h, p)); s.sendall(...); s.recv(1024)`
