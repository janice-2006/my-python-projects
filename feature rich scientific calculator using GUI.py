import tkinter as tk
from tkinter import ttk
from math import sin, cos, tan, log, log10, exp, pow, factorial, sqrt, radians, degrees, pi, e

class AdvancedCalculator:
    def _init_(self, root):
        self.root = root
        self.root.title("Advanced Scientific Calculator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)

        # Variable for toggling degrees/radians
        self.is_degree = True

        # History of calculations
        self.history = []

        # Memory value
        self.memory = 0

        # Display
        self.display = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # History display
        self.history_box = tk.Listbox(root, height=5, font=("Arial", 12))
        self.history_box.grid(row=1, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

        # Buttons
        self.create_buttons()

        # Configure grid weights
        for i in range(8):
            self.root.rowconfigure(i, weight=1)
        for i in range(5):
            self.root.columnconfigure(i, weight=1)

    def create_buttons(self):
        buttons = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3), ("C", 2, 4),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3), ("√", 3, 4),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3), ("^", 4, 4),
            ("0", 5, 0), (".", 5, 1), ("+", 5, 2), ("=", 5, 3), ("M+", 5, 4),
            ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("log", 6, 3), ("M-", 6, 4),
            ("(", 7, 0), (")", 7, 1), ("ln", 7, 2), ("e^x", 7, 3), ("MC", 7, 4),
            ("π", 8, 0), ("e", 8, 1), ("rad/deg", 8, 2), ("!", 8, 3), ("Mod", 8, 4),
        ]

        for (text, row, col) in buttons:
            tk.Button(
                self.root, text=text, font=("Arial", 16),
                command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, char):
        if char == "=":
            self.calculate_result()
        elif char == "C":
            self.display.delete(0, tk.END)
        elif char == "√":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, sqrt(value))
            except:
                self.display_error()
        elif char == "^":
            self.display.insert(tk.END, "")
        elif char == "M+":
            try:
                self.memory += float(self.display.get())
            except:
                self.display_error()
        elif char == "M-":
            try:
                self.memory -= float(self.display.get())
            except:
                self.display_error()
        elif char == "MC":
            self.memory = 0
        elif char == "π":
            self.display.insert(tk.END, pi)
        elif char == "e":
            self.display.insert(tk.END, e)
        elif char == "sin":
            self.handle_trigonometric("sin")
        elif char == "cos":
            self.handle_trigonometric("cos")
        elif char == "tan":
            self.handle_trigonometric("tan")
        elif char == "log":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, log10(value))
            except:
                self.display_error()
        elif char == "ln":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, log(value))
            except:
                self.display_error()
        elif char == "e^x":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, exp(value))
            except:
                self.display_error()
        elif char == "rad/deg":
            self.is_degree = not self.is_degree
        elif char == "!":
            try:
                value = int(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, factorial(value))
            except:
                self.display_error()
        elif char == "Mod":
            self.display.insert(tk.END, "%")
        else:
            self.display.insert(tk.END, char)

    def handle_trigonometric(self, func):
        try:
            value = float(self.display.get())
            if self.is_degree:
                value = radians(value)
            if func == "sin":
                result = sin(value)
            elif func == "cos":
                result = cos(value)
            elif func == "tan":
                result = tan(value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        except:
            self.display_error()

    def calculate_result(self):
        try:
            expression = self.display.get()
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.history.append(expression + " = " + str(result))
            self.update_history()
        except:
            self.display_error()

    def update_history(self):
        self.history_box.delete(0, tk.END)
        for item in self.history[-5:]:
            self.history_box.insert(tk.END, item)

    def display_error(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, "Error")

# Main execution
if _name_ == "_main_":
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()