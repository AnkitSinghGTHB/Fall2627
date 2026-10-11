# ⏱️ CSE3011: Python Emergency Plan & Master Code Blueprints

> **Exam Date**: Monday, October 19, 2026 (01:15 PM – 04:15 PM)  
> **Pre-TEE Position**: +3.3 marks ahead of class! Needs only **62–66 / 100** in TEE for A Grade.  
> **Study Window**: Sunday, October 18 (Afternoon & Evening)

---

## 🎯 The 5 Master Code Blueprints (Guaranteed 60+ Marks)

### Blueprint 1: Operator Overloading OOP Class (`__add__`, `__str__`) (Unit 3 - 12 Marks)
```python
class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}j"

# Test: c1 = ComplexNumber(2, 3); c2 = ComplexNumber(4, 5); print(c1 + c2) -> "6 + 8j"
```

---

### Blueprint 2: File Word Frequency Counter & Dictionary Formatting (Unit 4 - 8/12 Marks)
```python
def count_word_frequencies(filename):
    freq = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.lower().strip().split():
                clean_word = "".join(c for c in word if c.isalnum())
                if clean_word:
                    freq[clean_word] = freq.get(clean_word, 0) + 1
    return dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
```

---

### Blueprint 3: SQLite3 Database CRUD Operations (Unit 4 - 12 Marks)
```python
import sqlite3

def manage_student_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            gpa REAL
        )
    """)
    # Parameterized insertion (prevents SQL injection)
    cursor.execute("INSERT OR REPLACE INTO students VALUES (?, ?, ?)", (101, "Ankit", 9.2))
    conn.commit()

    cursor.execute("SELECT * FROM students WHERE gpa >= ?", (9.0,))
    rows = cursor.fetchall()
    conn.close()
    return rows
```

---

### Blueprint 4: Tkinter GUI Event-Driven Application (Unit 5 - 12 Marks)
```python
import tkinter as tk
from tkinter import messagebox

def create_gui_app():
    root = tk.Tk()
    root.title("Registration Form")
    root.geometry("300x200")

    tk.Label(root, text="Enter Name:").pack(pady=5)
    entry_name = tk.Entry(root)
    entry_name.pack(pady=5)

    def on_submit():
        name = entry_name.get()
        if name:
            messagebox.showinfo("Success", f"Welcome, {name}!")
        else:
            messagebox.showwarning("Warning", "Name cannot be empty!")

    tk.Button(root, text="Submit", command=on_submit).pack(pady=10)
    root.mainloop()
```

---

### Blueprint 5: Multi-threaded Shared Resource Synchronization (Unit 5 - 8 Marks)
```python
import threading

balance = 1000
lock = threading.Lock()

def withdraw(amount):
    global balance
    with lock:  # Automatically acquires and releases lock
        if balance >= amount:
            balance -= amount
            print(f"Withdrew {amount}, New Balance: {balance}")
        else:
            print("Insufficient Funds!")

t1 = threading.Thread(target=withdraw, args=(600,))
t2 = threading.Thread(target=withdraw, args=(500,))
t1.start(); t2.start()
t1.join(); t2.join()
```
