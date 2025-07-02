# 📟 Vic Advanced Calculator v1.2

![image](https://github.com/user-attachments/assets/68ec1f96-ae90-4ddf-a4eb-f6e83d917325)


**Vic Advanced Calculator** is a modern and intelligent desktop calculator built with **Python** and **Tkinter**, supporting both standard and scientific calculations, AI-assisted problem-solving (via OpenAI GPT-4o), and power-state simulation. The latest version (v1.2) adds icon support for PyInstaller builds, implements a persistent power control system, and introduces the `Ans` variable to reuse previous results in real-time calculations.

---

## ✨ Key Features (v1.2)

- ✅ **Standard Arithmetic Operations**: `+`, `-`, `*`, `/`, `=`, `sqrt`, `Back`
- 🧠 **AI Assistant via ChatGPT (GPT-4o)**: Solves complex math using OpenAI
- 🔁 **Ans Variable**: Recall the last result using `Ans` in subsequent expressions
- 🕹️ **ON/OFF Simulation**: Disables calculator logic and GUI on power OFF
- 🕒 **Check Time Button**: Displays current system time in AM/PM format
- 🎨 **Custom App Icon**: Supports `.ico` file through `resource_path()` for PyInstaller
- 📦 **EXE-Ready Architecture**: Uses `resource_path()` for asset bundling
- 🖥️ **Zoomed Startup**: Launches in fullscreen using `root.state("zoomed")`
- 🛡️ **Safe Error Handling**: Protects users from invalid expressions or empty operations
- 🔒 **Read-Only AI Output**: Lock AI result field to prevent editing
- 🔤 **Backspace Button**: Removes last input character
- 💻 **Pythonic Parsing with AST**: Ensures secure evaluation of expressions

---

## 🆕 What’s New in v1.2

| Feature              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `ON/OFF Power`       | Now functional; disables all input when OFF, and re-enables when ON         |
| `Ans` Support        | Typing an operator after evaluation uses `Ans` as previous result           |
| `resource_path()`    | Lets you bundle assets (like `.ico`) correctly for `.exe` using PyInstaller |
| `vcal.ico` Support   | Calculator now loads a custom icon in both script and compiled form         |
| GUI Improvements     | Improved reliability, startup behavior, and reduced clutter                 |
| `display_label1`     | Displays the output/result; reset on ON/OFF                                |

---

## 📦 Project Structure

```
VicAdvancedCalculator/
│
├── VicAdvancedCalculator_v1.0.py   # Initial version
├── VicAdvancedCalculator_v1.1.py   # Chained result, better layout
├── VicAdvancedCalculator_v1.2.py   # Adds ON/OFF, Ans, .ico, PyInstaller support
├── VicAdvancedCalculator_v1.3.py   # (Future/working version)
│
├── vcal.ico                        # App icon used in v1.2+
├── README.md                       # Project documentation (markdown)
├── requirements.txt                # Python dependencies (openai, etc.)
├── LICENSE                         # MIT License (or LICENSE.txt if that’s your style)
│
└──
```






---

## 🛠 Requirements

- Python **3.8 or later**
- OpenAI account & API key
- Internet connection (for AI assistant)
- Required libraries:
  ```bash
  pip install openai




Optional for .exe creation:
pip install pyinstaller




### 🧪 Installation & Running
### ▶️ Run Normally

```
python vic_calculator_v1.2.py
```


## 🛠️ Build EXE (Windows)
```
pyinstaller --onefile --windowed --icon=vcal.ico vic_calculator_v1.2.py
```

## ✅ App icon and assets will load automatically using the resource_path() helper.

### 💡 Example Usage
### ➕ Basic Operations
Click:

```
7 → + → 3 → =
Output: 10
```

### 🔁 Using Previous Result (Ans)
### Evaluate an expression like:

```
6 * 4 = 24
Now press:


+ → 3 → =
It becomes: Ans + 3 → 24 + 3 → 27
```
### √ Square Root
Press:


sqrt
Calculates the square root of the last result or current input.

⏱ Check Time
Click Check Time to toggle display of system time.

### 🤖 Ask AI
```Type: Solve: integral of x^2```

Click Ask AI

Wait for a GPT-4o-generated answer.

## 🔐 Safety & Design
Input is filtered through ast.parse() to avoid unsafe eval()

AI Output is locked with tk.DISABLED to prevent accidental edits

try/except blocks wrap all core logic for safe error messaging

Icons and assets resolve using resource_path() for compatibility with PyInstaller

# 🔮 Future Plans (v1.3+)
📊 Graph plotting (line, bar, equation-based)

📓 Calculation history (local or session-based)

🎭 Scientific functions: sin, cos, tan, log, exp, etc.

🧩 Modular plugin support for new tools

🌘 Dark mode & themes


# 👨‍💻 Author
[Victor Godwin](https://github.com/Vic-Godwin)
📧 Email: [Victor Godwin](mailto:vicgodwin95@gmail.com)

📄 License
MIT License.
Feel free to fork, use, and contribute — just credit the author where appropriate.

## 🧠 Tip for Developers
When building with PyInstaller and using an icon:


```.iconbitmap(resource_path("vcal.ico"))```
This ensures the icon loads whether you're running the script or an .exe.
