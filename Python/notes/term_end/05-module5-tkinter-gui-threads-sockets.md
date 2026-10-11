# 📘 Unit 5: Tkinter GUI, Multithreading & Network Sockets

---

## 1. Python Graphical User Interface (GUI) Ecosystem

Python provides multiple toolkits for developing desktop graphical user interfaces:

| GUI Library | Architecture / Backend | Key Features & Target Use Cases |
|:---|:---|:---|
| **Tkinter** | Standard Tk GUI toolkit shipped built-in with Python | Native, lightweight, zero-dependency; default choice for academic and small-to-medium utility apps. |
| **wxPython** | C++ `wxWidgets` cross-platform toolkit wrapper | True native look-and-feel across Windows, macOS, and Linux; richer widget set than Tkinter. |
| **JPython / Jython** | Python implementation written in and running on Java Virtual Machine (JVM) | Provides seamless 2-way interoperability between Python scripts and enterprise Java class libraries (Swing/AWT). |
| **PyQt / PySide** | C++ Qt framework bindings (PyQt: Riverbank GPL; PySide: Official Qt LGPL) | Industrial-grade, modern desktop applications with visual design tools (Qt Designer), hardware acceleration, and CSS styling. |
| **Kivy** | OpenGL ES accelerated cross-platform library | Designed for novel multi-touch user interfaces, mobile apps (Android/iOS), and interactive kiosk displays. |
| **Turtle** | Built-in Tkinter-based canvas graphics | Introductory vector graphics and visual geometry programming. |

---

### 1.1 The Event-Driven Architecture
In event-driven GUI programming, code execution is determined by asynchronous user interactions (mouse clicks, key presses, window resizing) triggering designated callback handler functions.

```
+-----------------------------------------------------------------------------------------+
|                               TKINTER GEOMETRY MANAGERS                                 |
+---------------------+---------------------------------+---------------------------------+
| Manager             | Mechanics                       | Primary Configuration Options   |
+---------------------+---------------------------------+---------------------------------+
| **`pack()`**        | Packs widgets against cavity    | `side=TOP/BOTTOM/LEFT/RIGHT`,   |
|                     | boundaries in sequential flow   | `fill=BOTH/X/Y`, `expand=True`  |
+---------------------+---------------------------------+---------------------------------+
| **`grid()`**        | Arranges widgets in a 2D table  | `row`, `column`, `rowspan`,     |
|                     | grid of rows and columns        | `columnspan`, `sticky='nsew'`   |
+---------------------+---------------------------------+---------------------------------+
| **`place()`**       | Positions widgets using exact   | `x`, `y`, `width`, `height`,    |
|                     | pixel or relative coordinates   | `relx`, `rely`                  |
+---------------------+---------------------------------+---------------------------------+
```

### 1.2 Complete Working Tkinter Arithmetic Calculator
```python
import tkinter as tk

def create_calc():
    root = tk.Tk()
    root.title("Simple Adder")
    root.geometry("260x180")

    tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
    e1 = tk.Entry(root)
    e1.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)
    e2 = tk.Entry(root)
    e2.grid(row=1, column=1, padx=5, pady=5)

    lbl_result = tk.Label(root, text="Result: --", font=("Arial", 11, "bold"))
    lbl_result.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate():
        try:
            val = float(e1.get()) + float(e2.get())
            lbl_result.config(text=f"Result: {val}")
        except ValueError:
            lbl_result.config(text="Error: Enter valid numbers!")

    tk.Button(root, text="Add (+)", command=calculate, bg="#4CAF50", fg="white").grid(row=2, column=0, columnspan=2, pady=5)
    root.mainloop()
```

---

## 2. Multithreading & Synchronization

### 2.1 The Global Interpreter Lock (GIL)
CPython enforces a mutex called the **GIL**, ensuring that only one native OS thread executes Python bytecode at any given moment.
* *Impact*: Multithreading does not achieve multicore parallel speedup for CPU-bound computations (use the `multiprocessing` module instead).
* *Strength*: Multithreading provides massive concurrency benefits for **I/O-bound tasks** (network requests, database operations, file reading).

### 2.2 Thread Lifecycle & Synchronization using `Lock`
```python
import threading, time

counter = 0
lock = threading.Lock()

def worker():
    global counter
    for _ in range(100000):
        with lock:  # Critical section protected against race conditions
            counter += 1

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

t1.start(); t2.start()
t1.join();  t2.join()  # Main thread waits for both workers to finish
print("Final Synchronized Counter:", counter)  # Guaranteed 200,000
```

---

## 3. Network Programming: BSD Sockets API

### 3.1 TCP Echo Server (`socket` Module)
```python
import socket

def run_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
    server_sock.bind(("127.0.0.1", 65432))
    server_sock.listen(5)
    print("Server listening on port 65432...")

    client_conn, client_addr = server_sock.accept()
    print(f"Connected by client: {client_addr}")

    data = client_conn.recv(1024)
    print(f"Received from client: {data.decode('utf-8')}")

    client_conn.sendall(b"ACK from Python Server")
    client_conn.close()
    server_sock.close()
```

### 3.2 TCP Echo Client
```python
import socket

def run_client():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(("127.0.0.1", 65432))
    
    client_sock.sendall(b"Hello Server from Ankit!")
    response = client_sock.recv(1024)
    print(f"Server replied: {response.decode('utf-8')}")
    
    client_sock.close()
```

---

## 4. CGI (Common Gateway Interface) Web Programming

### 4.1 Architecture & Workflow
CGI is a standard protocol enabling web servers (such as Apache in XAMPP) to execute external command-line programs (Python scripts) and dynamically generate web pages:

```
[ Browser Client ]  ──(HTTP POST/GET)──▶  [ Web Server (Apache/XAMPP) ]
                                                   │
                                            Executes script (.py)
                                                   ▼
[ Browser Displays HTML ] ◀──(HTTP HTML)──  [ Python CGI Script ]
```

### 4.2 Script Requirements
1. **Shebang Line**: First line pointing to the Python interpreter:
   `#!C:/Users/Admin/AppData/Local/Programs/Python/Python39/python.exe`
2. **HTTP Header**: Output header separated by a blank line (`\r\n\r\n`):
   `print("Content-type: text/html\r\n\r\n")`
3. **HTML Payload**: Printed directly to `sys.stdout`.
4. **Form Data Handling**: Using the standard `cgi` module and `cgi.FieldStorage()`.

### 4.3 Working CGI Form Handler (`student_register.py`)
```python
#!C:/Python310/python.exe
import cgi
import html

# Required HTTP Header
print("Content-type: text/html\r\n\r\n")

print("""<!DOCTYPE html>
<html>
<head><title>Student Registration Response</title></head>
<body style="font-family: Arial; padding: 20px;">
<h2>Student Registration Confirmation</h2>""")

# Parse form data sent via POST/GET
form = cgi.FieldStorage()

name = html.escape(form.getvalue("student_name", "Anonymous"))
reg_no = html.escape(form.getvalue("reg_no", "Not Provided"))
branch = html.escape(form.getvalue("branch", "General"))

print(f"""
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <tr><th>Field</th><th>Submitted Value</th></tr>
  <tr><td>Student Name</td><td>{name}</td></tr>
  <tr><td>Registration No</td><td>{reg_no}</td></tr>
  <tr><td>Branch</td><td>{branch}</td></tr>
</table>
<p style="color: green; font-weight: bold;">Record successfully processed by Python CGI!</p>
</body>
</html>
""")
```

### 4.4 Local vs Remote Server Deployment (XAMPP Steps)
1. Launch **XAMPP Control Panel** and start the Apache server.
2. In Apache configuration (`httpd.conf`), enable CGI execution (`AddHandler cgi-script .py`, `Options +ExecCGI`).
3. Add the exact path to `python.exe` at the top (shebang line) of the `.py` file.
4. Save the script inside `C:\xampp\htdocs\` or `C:\xampp\cgi-bin\`.
5. Access via browser URL: `http://localhost/student_register.py` or `http://127.0.0.1/cgi-bin/...`.

---

## 5. Pygame Interactive 2D Simulations

### 5.1 Pygame Game Loop Architecture
Every Pygame application follows a 4-phase cyclic execution model:
1. **Event Polling**: `pygame.event.get()` detects window close (`QUIT`), keyboard, and mouse inputs.
2. **Physics & State Update**: Update positions ($x \mathrel{+}= v_x$, $y \mathrel{+}= v_y$).
3. **Render / Blit**: Clear screen (`screen.fill()`), draw shapes (`pygame.draw.circle/ellipse`), update display (`pygame.display.flip()`).
4. **Frame Rate Throttling**: `clock.tick(60)` caps execution at 60 FPS.

---

## 6. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Write a complete client-server program in Python using the `socket` module where the client sends a string to the server, and the server reverses the string and sends it back to the client.**

**Solution**:
1. **Server Program (`server.py`)**:
```python
import socket

def reverse_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen(1)
    print("Reverse Server is ready on port 9999...")

    conn, addr = server.accept()
    print(f"Client connected from {addr}")

    data = conn.recv(1024).decode("utf-8")
    reversed_data = data[::-1]  # Reverse string
    conn.sendall(reversed_data.encode("utf-8"))

    conn.close()
    server.close()

if __name__ == "__main__":
    reverse_server()
```
2. **Client Program (`client.py`)**:
```python
import socket

def reverse_client(message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))

    client.sendall(message.encode("utf-8"))
    reversed_message = client.recv(1024).decode("utf-8")

    print(f"Original: {message}")
    print(f"Reversed: {reversed_message}")
    client.close()

if __name__ == "__main__":
    reverse_client("Python Programming")
    # Output: Reversed: gnimmargorP nohtyP
```

### Question 2 (8 Marks)
**Explain the role of geometry managers in Tkinter. Compare `pack()`, `grid()`, and `place()` with code examples.**

**Solution**:
1. **Role of Geometry Managers**: Organize widget layout, alignment, and resizing behavior within parent containers.
2. **Comparison**:
   - `pack()`: Stacks widgets along edges (e.g., `btn.pack(side=tk.TOP, fill=tk.X)`). Ideal for simple vertical/horizontal flows.
   - `grid()`: Places widgets in structured 2D matrices with rows and columns (e.g., `btn.grid(row=1, column=0, sticky="ew")`). Standard for forms and data entry.
   - `place()`: Explicit pixel positioning (e.g., `btn.place(x=50, y=100)`). High control but fragile across dynamic window resizing.

---

### Question 3 (12 Marks) [Direct from List of Experiments 4]
**(a) Write a Python program to simulate elliptical orbits using Pygame.**  
**(b) Write a Python program to simulate a bouncing ball with gravity and boundary collision in Pygame.**

**Solution**:
#### (a) Elliptical Orbit Simulation (`elliptical_orbit.py`):
```python
import pygame
import math
import sys

def run_elliptical_orbit():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Elliptical Orbit Simulation")
    clock = pygame.time.Clock()

    # Ellipse geometric parameters
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    semi_major = 250   # Semi-major axis (a)
    semi_minor = 140   # Semi-minor axis (b)
    angle = 0.0        # Theta parameter in radians
    angular_speed = 0.03

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear background to dark space
        screen.fill((10, 15, 30))

        # Draw central star (Sun) at center
        pygame.draw.circle(screen, (255, 200, 0), (center_x, center_y), 24)

        # Draw orbital path (ellipse guide)
        orbit_rect = pygame.Rect(center_x - semi_major, center_y - semi_minor, 
                                 semi_major * 2, semi_minor * 2)
        pygame.draw.ellipse(screen, (70, 70, 100), orbit_rect, 1)

        # Parametric equations of ellipse: x = h + a*cos(θ), y = k + b*sin(θ)
        planet_x = center_x + int(semi_major * math.cos(angle))
        planet_y = center_y + int(semi_minor * math.sin(angle))

        # Draw orbiting planet
        pygame.draw.circle(screen, (0, 180, 255), (planet_x, planet_y), 12)

        angle += angular_speed
        if angle >= 2 * math.pi:
            angle -= 2 * math.pi

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run_elliptical_orbit()
```

#### (b) Bouncing Ball Simulation (`bouncing_ball.py`):
```python
import pygame
import sys

def run_bouncing_ball():
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball Physics Simulation")
    clock = pygame.time.Clock()

    # Ball properties
    radius = 20
    x, y = WIDTH // 2, 80
    vx = 4           # Horizontal velocity
    vy = 0           # Vertical velocity
    gravity = 0.5    # Downward acceleration
    damping = 0.85   # Energy retained on bounce

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Physics update
        vy += gravity
        x += vx
        y += vy

        # Floor collision
        if y + radius >= HEIGHT:
            y = HEIGHT - radius
            vy = -vy * damping
            # Stop micro-bouncing
            if abs(vy) < 1.0:
                vy = 0

        # Wall collisions
        if x - radius <= 0 or x + radius >= WIDTH:
            vx = -vx

        # Render
        screen.fill((240, 240, 245))
        # Draw ground line
        pygame.draw.line(screen, (50, 50, 50), (0, HEIGHT - 1), (WIDTH, HEIGHT - 1), 3)
        # Draw red ball
        pygame.draw.circle(screen, (220, 50, 50), (int(x), int(y)), radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run_bouncing_ball()
```
