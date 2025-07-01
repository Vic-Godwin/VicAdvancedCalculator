import datetime
import tkinter as tk
from tkinter import scrolledtext
import ast
import threading
import openai
import re
import math

# Initialize OpenAI (put your actual API key below)
client = openai.OpenAI(api_key="my-api-key")

# Global result to chain calculations
last_result = None

def advanced_calculator():
    """Runs ChatGPT AI solving in a separate thread"""
    threading.Thread(target=solve_math_problem, daemon=True).start()

def solve_math_problem():
    """Handles ChatGPT assistant solving math expressions"""
    math_problem = chat_input.get()
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"Solve: {math_problem}"}]
        )
        solution = response.choices[0].message.content
        
        # Display ChatGPT output properly with correct enabling/disabling
        chat_output.config(state=tk.NORMAL)
        chat_output.insert("end", solution + "\n")
        chat_output.config(state=tk.DISABLED)
    except Exception as e:
        chat_output.config(state=tk.NORMAL)
        chat_output.delete("1.0", "end")
        chat_output.insert("end", f"Error: {str(e)}")
        chat_output.config(state=tk.DISABLED)

def show_time():
    """Toggles display of current system time"""
    text = display_btn.cget("text")
    if text == "Check Time":
        get_datetime = datetime.datetime.now()
        real_time = re.findall(r"\d{2}:\d{2}", str(get_datetime))[0]
        hour = int(real_time.split(":")[0])
        suffix = "PM" if hour >= 12 else "AM"
        display_btn.config(text=real_time + suffix, font=("BankGothic Md BT", 16), bg="#E67E22")
    else:
        display_btn.config(text="Check Time", font=font_small, bg=button_color)

def numbers(num):
    """Handles calculator button input"""
    global last_result
    screen_text = display_label.cget("text")
    
    # Turn ON
    if num == "ON":
        display_label.config(text="")
        display_label1.config(text="0")
        return

    # Turn OFF
    if num == "OFF":
        display_label.config(text="")
        display_label1.config(text="")
        return

    # Backspace
    if num == "Back":
        display_label.config(text=screen_text[:-1])
        return

    # Square root
    if num == "sqrt":
        try:
            value = display_label1.cget("text") or display_label.cget("text")
            result = math.sqrt(float(value))
            display_label1.config(text=str(result))
            display_label.config(text="")
            last_result = result  # Store result for chaining
        except Exception as e:
            display_label1.config(text=f"Error: {str(e)}")
        return

    # Evaluate expression
    if num == "=":
        try:
            node = ast.parse(screen_text, mode="eval")
            result = eval(compile(node, "<string>", mode="eval"))
            display_label1.config(text=str(result))
            display_label.config(text="")
            last_result = result
        except Exception as e:
            display_label1.config(text=f"Error: {str(e)}")
        return

    # Handle operator after result
    if num in ["+", "-", "*", "/"]:
        if not screen_text and last_result is not None:
            display_label.config(text=str(last_result) + num)
        else:
            display_label.config(text=screen_text + num)
        return

    # Append digits or "."
    display_label.config(text=screen_text + str(num))


# ==== GUI SETUP ====

root = tk.Tk()
root.title("Vic Advanced Calculator")
root.state("zoomed")  # Full-screen

# COLORS & FONTS
bg_color = "#2C3E50"
button_color = "#34495E"
button_text_color = "white"
display_color = "#ECF0F1"
font_large = ("Arial", 24)
font_small = ("Arial", 16)

# ==== Display Section ====
display_frame = tk.Frame(root, bg=display_color)
display_frame.pack(fill="x", padx=20, pady=10)

display_label = tk.Label(display_frame, text="", font=font_large, bg=display_color, fg="black",
                         anchor="nw", height=1, padx=10)
display_label.pack(fill="x")

display_btn = tk.Button(display_frame, text="Check Time", font=font_small, bg=button_color,
                        fg="white", width=3, command=show_time)
display_btn.pack(fill="x", side="left", expand=True, padx=5)

display_label1 = tk.Label(display_frame, text="", font=font_large, bg=display_color, fg="black",
                          anchor="ne", height=1, padx=10, width=50)
display_label1.pack(fill="x", side="right", expand=True, padx=5)

# ==== Calculator Buttons ====
buttons_frame = tk.Frame(root, bg=bg_color)
buttons_frame.pack(fill="both", expand=True)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

for row in buttons:
    row_frame = tk.Frame(buttons_frame, bg=bg_color)
    row_frame.pack(fill="both", expand=True)
    for val in row:
        btn = tk.Button(row_frame, text=val, font=font_small, bg=button_color, fg=button_text_color,
                        width=5, height=2, command=lambda text=val: numbers(text))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

# ==== Scientific Buttons ====
sci_buttons_frame = tk.Frame(root, bg=bg_color)
sci_buttons_frame.pack(fill="x", padx=20, pady=5)

sci_buttons = ["sin", "cos", "tan", "log", "sqrt", "π", "Back", "OFF", "ON"]
for val in sci_buttons:
    btn = tk.Button(sci_buttons_frame, text=val, font=font_small, bg="#1ABC9C", fg="black", width=8,
                    height=2, command=lambda text=val: numbers(text))
    btn.pack(side="left", expand=True, padx=2, pady=2)

# ==== ChatGPT Assistant ====
chat_frame = tk.Frame(root, bg=bg_color)
chat_frame.pack(fill="x", padx=20, pady=10)

chat_label = tk.Label(chat_frame, text="ChatGPT Math Assistant", font=font_small, bg=bg_color, fg="white")
chat_label.pack(anchor="w")

chat_input = tk.Entry(chat_frame, font=font_small, width=50)
chat_input.pack(side="left", expand=True, fill="x", padx=5)

chat_btn = tk.Button(chat_frame, text="Ask AI", font=font_small, bg="#E67E22",
                     fg="white", width=10, command=solve_math_problem)
chat_btn.pack(side="right", padx=5)

chat_output = scrolledtext.ScrolledText(root, font=("Arial", 14), height=5)
chat_output.pack(fill="both", padx=20, pady=5, expand=True)
chat_output.config(state=tk.DISABLED)  # Output area starts locked

# ==== Run VicAvanced Calculator App ====
root.mainloop()
