# ⚡ CAT-2 HOTS Master Crib — Module 4: Files, Exceptions & Database Connectivity
**Course**: CSE3011 — Python Programming  
**Coverage**: File Streams, System OS Operations, Exception Handling & DB APIs | **Exam Mode**: Open Book  
**Target Score**: 45+ / 50 (S-Grade Boundary)

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Mentions / Shows... | It Means This Exact Topic | Your Immediate Formula / Action |
| :--- | :--- | :--- |
| "Word frequency analysis from file" | **File Text Processing** | `open(file, 'r')` $\to$ `collections.Counter` or dictionary $\to$ sort by frequency $\to$ write to output file. |
| "Student records file handling", CSV | **Structured Records Processing** | Format: `ID,Name,Marks`. Split by delimiter, compute average/grade, write back with headers. |
| "Demonstrate try, except, else, finally" | **Robust Exception Handling** | `try`: risky code; `except`: error handler; `else`: runs if NO exception; `finally`: cleanup (always runs!). |
| "OS operations: create, rename, check, delete" | **`os` & `pathlib` Operations** | `os.path.exists()`, `os.rename()`, `os.remove()`, `os.listdir()`, `os.path.getsize()`. |
| "Database connectivity", SQLite / MySQL | **Python DB-API 2.0** | `conn = sqlite3.connect()`, `cursor = conn.cursor()`, parameterized query `cursor.execute('... ?', (val,))`, `conn.commit()`. |

---

## 🛠️ TIER 2: Master Solved Code Recipes (Directly Answering Activity 3)

### Recipe 4.1: Word Frequency Analysis & File Output
*(Direct solution to Activity 3 Question 1 & Experiment 8)*
```python
import string
from collections import Counter

def word_frequency_analysis(input_filepath: str, output_filepath: str):
    """Reads a text file, cleans punctuation, counts word frequencies, and writes sorted results."""
    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            text = infile.read().lower()

        # Remove punctuation
        cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
        words = cleaned_text.split()

        # Count frequencies
        freq_counter = Counter(words)

        # Write results to output file
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(f"{'WORD':<20} | {'FREQUENCY':<10}\n")
            outfile.write("-" * 35 + "\n")
            for word, count in freq_counter.most_common():
                outfile.write(f"{word:<20} | {count:<10}\n")

        print(f"Analysis complete! Results written to {output_filepath}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' does not exist.")
    except PermissionError:
        print("Error: Permission denied while accessing file.")
```

---

### Recipe 4.2: Student Records Management with File Handling
*(Direct solution to Activity 3 Question 2)*
```python
def process_student_records(input_file: str, report_file: str):
    """Reads student records (RegNo, Name, Marks), computes grades, and writes report."""
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        processed_records = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            reg_no, name, marks_str = [item.strip() for item in line.split(',')]
            marks = float(marks_str)
            
            # Determine grade
            if marks >= 90: grade = 'S'
            elif marks >= 80: grade = 'A'
            elif marks >= 70: grade = 'B'
            elif marks >= 60: grade = 'C'
            elif marks >= 50: grade = 'D'
            else: grade = 'F'

            processed_records.append((reg_no, name, marks, grade))

        # Write output report
        with open(report_file, 'w', encoding='utf-8') as outfile:
            outfile.write(f"{'REG NO':<15} | {'NAME':<20} | {'MARKS':<8} | {'GRADE':<6}\n")
            outfile.write("=" * 55 + "\n")
            for reg, nm, mk, gd in processed_records:
                outfile.write(f"{reg:<15} | {nm:<20} | {mk:<8.1f} | {gd:<6}\n")

    except FileNotFoundError:
        print(f"Source records file '{input_file}' not found.")
```

---

### Recipe 4.3: OS File Management Operations Suite
*(Direct solution to Activity 3 Question 4)*
```python
import os

def demonstrate_file_management(filename: str):
    """Demonstrates creating, checking, renaming, metadata querying, and deleting a file."""
    # 1. Create and write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Sample test data for OS file management.")
    print(f"1. Created: '{filename}'")

    # 2. Check if file exists
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        abs_path = os.path.abspath(filename)
        print(f"2. Exists: Yes | Size: {size} bytes | Path: {abs_path}")

    # 3. Rename file
    new_filename = "renamed_" + filename
    os.rename(filename, new_filename)
    print(f"3. Renamed to: '{new_filename}'")

    # 4. Delete file
    if os.path.exists(new_filename):
        os.remove(new_filename)
        print(f"4. Deleted: '{new_filename}'")
```

---

### Recipe 4.4: Generic Database Connectivity Pattern (SQLite / MySQL)
```python
import sqlite3

def init_and_query_database(db_name: str = "students.db"):
    """Demonstrates table creation, parameterized inserts, queries, and transactions."""
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Create table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reg_no TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                cgpa REAL
            )
        """)

        # Parameterized insert (Prevents SQL Injection!)
        student_data = [('24BCE1001', 'Danny', 9.2), ('24BCE1002', 'Thomas', 8.7)]
        cursor.executemany("INSERT OR IGNORE INTO students (reg_no, name, cgpa) VALUES (?, ?, ?)", student_data)
        conn.commit()

        # Query
        cursor.execute("SELECT reg_no, name, cgpa FROM students WHERE cgpa >= ?", (9.0,))
        top_students = cursor.fetchall()
        print("Top Students:", top_students)

    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed cleanly.")
```
