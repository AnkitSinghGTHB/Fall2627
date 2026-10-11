# 📘 Unit 4: File Handling, Object Persistence & Database Programming

---

## 1. File I/O & Pointer Manipulation

### 1.1 File Modes & Context Managers
* Always open files using the `with` statement (Python context manager protocol using `__enter__` and `__exit__`), which guarantees file descriptor closure even if exceptions occur.

```python
# Reading and writing text files
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()          # Reads entire file as string
    # lines = f.readlines()     # Reads entire file as list of line strings
    # line = f.readline()       # Reads a single line
```

### 1.2 File Pointer Navigation: `seek()` and `tell()`
* `f.tell()`: Returns the current integer byte offset position of the file pointer.
* `f.seek(offset, whence)`: Repositions the file pointer.
  - `whence = 0`: Relative to the beginning of the file (Default).
  - `whence = 1`: Relative to current pointer position (Requires binary mode `'rb'`).
  - `whence = 2`: Relative to the end of the file (Requires binary mode `'rb'`).

```python
with open("log.bin", "rb") as f:
    f.seek(0, 2)              # Move pointer to end of file
    file_size = f.tell()      # Returns exact file size in bytes
    f.seek(-10, 2)            # Move 10 bytes before end
    tail_bytes = f.read(10)
```

---

## 2. Object Persistence: JSON vs Pickle

| Dimension | `json` Module | `pickle` Module |
|:---|:---|:---|
| **Format** | Human-readable text (UTF-8 standard) | Proprietary Python binary serialization |
| **Interoperability**| Universally supported by JavaScript, Java, Go | **Python-specific only** |
| **Data Types** | Basic primitives: `dict`, `list`, `str`, `int`, `bool`, `None` | Arbitrary custom Python class instances, lambdas, functions |
| **Security Risk** | Safe to deserialize from untrusted sources | **Security vulnerability**: Deserializing malicious pickle executes arbitrary OS shell commands |

```python
import json, pickle

data = {"student": "Ankit", "semester": "Fall2627", "cgpa": 9.2}

# JSON serialization
json_str = json.dumps(data, indent=4)
restored_json = json.loads(json_str)

# Pickle serialization
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
with open("data.pkl", "rb") as f:
    restored_pickle = pickle.load(f)
```

---

## 3. Database Programming: Python DB-API 2.0 Standard

All relational database drivers in Python (SQLite, MySQL, PostgreSQL) follow the **PEP 249 (DB-API 2.0)** standardized workflow:

```
[ connect() ] ──▶ [ cursor() ] ──▶ [ execute(SQL, params) ] ──▶ [ fetchall() / commit() ] ──▶ [ close() ]
```

### 3.1 SQLite3 Complete Operational Script
```python
import sqlite3

def sqlite_demo():
    # 1. Establish connection and cursor
    conn = sqlite3.connect("university.db")
    cur = conn.cursor()

    # 2. Create Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            code TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            credits INTEGER
        )
    """)

    # 3. Parameterized INSERT (Safe against SQL Injection attacks)
    course_data = [
        ("CSE3011", "Python Programming", 3),
        ("CSE4005", "Machine Learning", 3),
        ("ECE2002", "Digital Logic Design", 4)
    ]
    cur.executemany("INSERT OR REPLACE INTO courses VALUES (?, ?, ?)", course_data)
    conn.commit()  # Persist changes to disk

    # 4. Query with filter
    cur.execute("SELECT code, title FROM courses WHERE credits >= ?", (3,))
    results = cur.fetchall()
    for code, title in results:
        print(f"Course: {code} | Title: {title}")

    # 5. Clean resource shutdown
    conn.close()
```

### 3.2 MySQL Connector Syntax
```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123",
    database="vit_bhopal"
)
cur = conn.cursor()
# MySQL uses %s placeholder instead of ?
cur.execute("SELECT * FROM students WHERE branch = %s", ("CSE",))
rows = cur.fetchall()
conn.close()
```

---

## 4. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Write a Python program that reads a text file named `input.txt`, counts the occurrence of each unique word (ignoring case and punctuation), and writes the sorted word frequency list (in descending order) to a new file named `frequency.txt`. Handle potential file I/O errors gracefully.**

**Solution**:
```python
import string

def generate_word_frequency(input_path, output_path):
    word_counts = {}
    
    try:
        with open(input_path, "r", encoding="utf-8") as infile:
            for line in infile:
                # Remove punctuation and convert to lowercase
                cleaned_line = line.translate(str.maketrans("", "", string.punctuation)).lower()
                words = cleaned_line.split()
                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1
                    
        # Sort by frequency descending
        sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
        
        with open(output_path, "w", encoding="utf-8") as outfile:
            outfile.write("WORD,FREQUENCY\n")
            for word, count in sorted_words:
                outfile.write(f"{word},{count}\n")
                
        print(f"Success! Frequency table written to {output_path}")
        
    except FileNotFoundError:
        print(f"Error: The source file '{input_path}' does not exist.")
    except PermissionError:
        print("Error: Permission denied while accessing files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call function: generate_word_frequency("input.txt", "frequency.txt")
```

### Question 2 (8 Marks)
**Explain the DB-API 2.0 workflow in Python. Why must developers use parameterized queries instead of string concatenation when executing SQL statements?**

**Solution**:
1. **DB-API 2.0 Workflow**: Detail `connect()`, `cursor()`, `execute()`, `commit()`, and `close()`.
2. **Parameterized Queries vs String Concatenation**:
   - String concatenation:
     ```python
     # VULNERABLE TO SQL INJECTION!
     cur.execute(f"SELECT * FROM users WHERE user = '{username}' AND pass = '{password}'")
     ```
     If an attacker passes `' OR '1'='1`, the query executes `SELECT * FROM users WHERE user = '' OR '1'='1'`, bypassing authentication entirely!
   - Parameterized query:
     ```python
     # 100% SECURE:
     cur.execute("SELECT * FROM users WHERE user = ? AND pass = ?", (username, password))
     ```
     The DB engine compiles the SQL query structure *before* binding variables, treating all inputs strictly as literal string values rather than executable SQL syntax.
