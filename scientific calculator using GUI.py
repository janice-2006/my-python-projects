import tkinter as tk
from math import sin, cos, tan, log, sqrt, factorial, radians, pi, e, pow
import matplotlib.pyplot as plt
import numpy as np


class FeatureRichCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Feature-Rich Scientific Calculator")
        self.root.geometry("500x700")
        self.current_input = ""
        self.history = []
        self.memory = None
        self.create_widgets()

    def create_widgets(self):
        # Display area
        self.display = tk.Entry(self.root, font=("Arial", 20), bd=10, justify="right")
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Button Layout
        buttons = [
            "7", "8", "9", "/", "C", "Plot",
            "4", "5", "6", "*", "M+", "Theme",
            "1", "2", "3", "-", "MR", "History",
            "0", ".", "=", "+", "MC", "Clear",
            "sin", "cos", "tan", "log", "sqrt", "^",
            "(", ")", "pi", "e", "x!", "Help",
        ]

        row, col = 1, 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.root, text=button, font=("Arial", 14), command=action, width=7, height=2).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 5:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == "C":
            self.current_input = ""
        elif char == "=":
            try:
                result = eval(self.current_input.replace("^", "**"))
                self.history.append(f"{self.current_input} = {result}")
                self.current_input = str(result)
            except Exception:
                self.current_input = "Error"
        elif char == "M+":
            if self.current_input:
                self.memory = eval(self.current_input)
        elif char == "MR":
            if self.memory is not None:
                self.current_input += str(self.memory)
        elif char == "MC":
            self.memory = None
        elif char == "x!":
            try:
                self.current_input = str(factorial(int(self.current_input)))
            except Exception:
                self.current_input = "Error"
        elif char == "sqrt":
            try:
                self.current_input = str(sqrt(eval(self.current_input)))
            except Exception:
                self.current_input = "Error"
        elif char == "log":
            try:
                self.current_input = str(log(eval(self.current_input)))
            except Exception:
                self.current_input = "Error"
        elif char in ["sin", "cos", "tan"]:
            try:
                radians_value = radians(eval(self.current_input))
                self.current_input = str(eval(f"{char}({radians_value})"))
            except Exception:
                self.current_input = "Error"
        elif char == "pi":
            self.current_input += str(pi)
        elif char == "e":
            self.current_input += str(e)
        elif char == "^":
            self.current_input += "^"
        elif char == "Plot":
            self.plot_graph()
        elif char == "History":
            self.show_history()
        elif char == "Theme":
            self.toggle_theme()
        elif char == "Clear":
            self.history = []
        elif char == "Help":
            self.show_help()
        else:
            self.current_input += char
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)

    def plot_graph(self):
        try:
            expression = self.current_input.replace("^", "**")
            x = np.linspace(-10, 10, 400)
            y = eval(expression)
            plt.plot(x, y)
            plt.title(f"Graph of {self.current_input}")
            plt.xlabel("x-axis")
            plt.ylabel("y-axis")
            plt.grid(True)
            plt.show()
        except Exception:
            self.current_input = "Error"
            self.update_display()

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("300x400")
        for entry in self.history:
            tk.Label(history_window, text=entry, font=("Arial", 12)).pack()

    def toggle_theme(self):
        current_bg = self.root.cget("bg")
        new_bg = "black" if current_bg == "SystemButtonFace" else "SystemButtonFace"
        new_fg = "white" if current_bg == "SystemButtonFace" else "black"
        self.root.configure(bg=new_bg)
        self.display.configure(bg=new_bg, fg=new_fg)
        for widget in self.root.winfo_children():
            widget.configure(bg=new_bg, fg=new_fg)

    def show_help(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Help")
        help_window.geometry("400x300")
        help_text = """Welcome to the Feature-Rich Scientific Calculator!
        Features:
        - Basic operations: +, -, *, /
        - Scientific functions: sin, cos, tan, log, sqrt, x!
        - Plot graphs using 'Plot' button.
        - Memory functions: M+, MR, MC
        - Toggle theme with 'Theme' button.
        - View calculation history with 'History' button.
        """
        tk.Label(help_window, text=help_text, font=("Arial", 12), justify="left").pack(pady=10, padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = FeatureRichCalculator(root)
    root.mainloop()

