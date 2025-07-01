import datetime
import tkinter as tk
from tkinter import scrolledtext
import ast
import threading
import openai
import re
import math
client = openai.OpenAI(api_key="")

def advanced_calculator():
    """Runs the API call in a separate thread to avoid freezing."""
    threading.Thread(target=solve_math_problem, daemon=True).start()
def solve_math_problem():
    """Get user input, process via OpenAI, and display output."""
    math_problem = chat_input.get()  # Extract text from ScrolledText

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"Solve: {math_problem}"}]
        )

        solution = response.choices[0].message.content  # key access

        chat_output.insert("end", solution)  # Display new output
    except Exception as e:
        chat_output.delete("1.0", "end")
        chat_output.insert("end", f"Error: {str(e)}")


place_font,text='',''
am_pm,text1 = '',''
def show_time():
    global text,am_pm,text1,place_font
    text = display_btn.cget("text")
    if text == "Check Time":
        get_datetime = datetime.datetime.now()
        time_text = str(get_datetime)
        get_time= r"\d{2}:\d{2}"
        real_time = re.findall(get_time, time_text)
        real_time = real_time[0]
        hour = r"\d{2}"
        am_pm = re.findall(hour, str(real_time))
        am_pm = am_pm[0]

        if int(am_pm) >= 12:
            text1 = "PM"
        if int(am_pm) < 12:
            text1 = "AM"
        place_font = ("BankGothic Md BT",16)
        bgColor = "#E67E22"
        text = real_time

    else:
        text = "Check Time"
        text1 = ''
        place_font = font_small
        bgColor = button_color
    display_btn.config(text=text + text1,font=place_font,bg=bgColor)




def numbers(num):
    
    screen_text = display_label.cget("text")
    display_label.config(text=screen_text + str(num))

    if num == "ON":
        display_label.config(text="")
        display_label1.config(text="0")

    if num == "OFF":
        display_label.config(text="")
        display_label1.config(text="")

    if num == "Back":
        text = screen_text[:-1]
        display_label.config(text=text)

    if num == "sqrt":
        if display_label1:
            screen_text = display_label1.cget("text")
            try:
                display_label1.config(text=math.sqrt(int(screen_text)))
                screen_text = display_label1.cget("text")
                display_label.config(text=str(screen_text))
            except Exception as e:
                display_label1.config(text=f"Error {str(e)}")
        else:
            screen_text = display_label.cget("text")
            display_label1.config(text=math.sqrt(int(screen_text)))
            

    if num == "=":
        global result
        try:
            node = ast.parse(screen_text, mode="eval")
            result = eval(compile(node, "<strings>", mode="eval"))
            display_label1.config(text=str(result))
            display_label.config(text="")
        except Exception as e:
            display_label1.config(text=f"Error: {str(e)}")
        return

    if result:
        if num in ["+","-","*","/"]:
            display_label.configure(text=str(result)+ num)#+str(sscreen_text))    




# Create main window
root = tk.Tk()
root.title("Vic Advanced Calculator")
root.state("zoomed")  # Full-screen mode

# Colors and Styles
bg_color = "#2C3E50"  # Dark background
button_color = "#34495E"  # Dark gray buttons
button_text_color = "white"
display_color = "#ECF0F1"  # Light display
font_large = ("Arial", 24)
font_small = ("Arial", 16)

# 1. Display Screen
display_frame = tk.Frame(root, bg=display_color)
display_frame.pack(fill="x", padx=20, pady=10)


display_label = tk.Label(display_frame, text="", font=font_large, bg=display_color, fg="black",
                         anchor="nw", height=1, padx=10)
display_label.pack(fill="x")


display_btn = tk.Button(display_frame, text="Check Time", font=font_small, bg=button_color,
                     anchor="n",fg="white", width=3,command=show_time)
display_btn.pack(fill="x",side="left",expand=True,padx=5)

display_label1 = tk.Label(display_frame,text="", font=font_large, bg=display_color, fg="black",
                         anchor="ne", height=1, padx=10,width=50)
display_label1.pack(fill="x",side="right", expand=True, padx=5)


# 2. Standard Calculator Buttons
buttons_frame = tk.Frame(root, bg=bg_color)
buttons_frame.pack(fill="both", expand=True)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

for row_values in buttons:
    row_frame = tk.Frame(buttons_frame, bg=bg_color)
    row_frame.pack(fill="both", expand=True)

    for value in row_values:
        btn = tk.Button(row_frame, text=value, font=font_small, bg=button_color, fg=button_text_color, width=5,
                        height=2, command=lambda text=value: numbers(text))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

# 3. Scientific Calculator Buttons
sci_buttons_frame = tk.Frame(root, bg=bg_color)
sci_buttons_frame.pack(fill="x", padx=20, pady=5)

sci_buttons = ["sin", "cos", "tan", "log", "sqrt", "π", "Back", "OFF", "ON"]

for value in sci_buttons:
    btn = tk.Button(sci_buttons_frame, text=value, font=font_small, bg="#1ABC9C", fg="black", width=8,
                    height=2,command=lambda text=value: numbers(text))
    btn.pack(side="left", expand=True, padx=2, pady=2)

# 4. ChatGPT Assistant Section
chat_frame = tk.Frame(root, bg=bg_color)
chat_frame.pack(fill="x", padx=20, pady=10)

chat_label = tk.Label(chat_frame, text="ChatGPT Math Assistant", font=font_small, bg=bg_color, fg="white")
chat_label.pack(anchor="w")

chat_input = tk.Entry(chat_frame, font=font_small, width=50)
chat_input.pack(side="left", expand=True, fill="x", padx=5)

chat_btn = tk.Button(chat_frame, text="Ask AI", font=font_small, bg="#E67E22",
                     fg="white", width=10,command=solve_math_problem)
chat_btn.pack(side="right", padx=5)

chat_output = scrolledtext.ScrolledText(root, font=("Arial", 14), height=5, state=tk.DISABLED)
chat_output.pack(fill="both", padx=20, pady=5, expand=True)

# Run main loop
root.mainloop()

