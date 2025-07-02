# 🔢 VicAdvanced Calculator
Added new features and updated code for v1.1.01 release

![image](https://github.com/user-attachments/assets/2f4fd2b5-f03b-4b9e-8179-d36bdfa09bfb)

**VicAdvanced Calculator** is a modern, AI-powered Python calculator with a fullscreen GUI built using Tkinter. It blends standard arithmetic and scientific functions with GPT-based AI support, intuitive time display, and result memory — all in a sleek, responsive interface.

---

## 🔧 Features (v1.1.01)

- 🧮 Basic arithmetic operations: `+`, `-`, `*`, `/`, `sqrt`
- 🔁 **Last Result Memory (`Ans`)** for chained expressions
- ⌛ Real-time system **Check Time** toggle
- 🔙 `Back`, **ON**, and **OFF** power buttons
- 🤖 GPT-4o-powered assistant for solving typed math queries
- 📋 Intelligent expression handling using `eval` and `ast`
- 🎨 Clean fullscreen UI with intuitive layout
- 🧼 Improved error handling, responsive layout, and better logic flow

---

## 🛠️ Coming Soon

- 📈 Graphing interface for plotting any function
- 🔢 Trigonometric and logarithmic button logic
- 📚 History saving and recall feature
- ✍️ Persistent `Ans` tag display (e.g., `Ans + 5`)

---

## 🧑‍💻 How to Use

1. **Run the App**  
   Open `VicAdvancedCalculator_v1.1.py` in Python 3.8+.

2. **Calculate**  
   - Click numbers/operators
   - Use `=` to evaluate
   - Use `sqrt` for square root
   - After solving, continue with the result using an operator (`Ans + 4`)

3. **Time Toggle**  
   Press **Check Time** to toggle current time display.

4. **AI Math Help**  
   - Type any expression in the input box
   - Click **Ask AI** to get GPT-powered solution in the console

5. **Control Buttons**  
   - `Back` deletes last character
   - `OFF` disables output and clears input
   - `ON` reactivates and resets the calculator

---

## 📝 Version History

| Version | Highlights                                                  |
|---------|-------------------------------------------------------------|
| v1.0    | Initial release with basic calculator, GPT, and time toggle |
| v1.1    | Added result memory, smarter logic, ON/OFF buttons, cleaner UI |

---

## 📦 Requirements

- Python 3.8+
- `tkinter` (preinstalled in Python)
- `openai`
- Built-in: `datetime`, `math`, `threading`, `re`, `ast`

Install dependencies with:

```bash
pip install openai
```

# 📁 Project Structure

```
VicAdvancedCalculator/
├── VicAdvancedCalculator_v1.0.py     # Initial version
├── VicAdvancedCalculator_v1.1.py     # Latest version (with memory & ON/OFF)
├── README.md                         # Project documentation
└── assets/                           # (Optional) icons, screenshots
```

# 👨‍🎓 Author
### Victor Godwin
Engineer • Coder • AI Enthusiast

Building tools that make life easier, smarter, and more human.

