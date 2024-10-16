import tkinter as tk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.fibo import fibonacci



def calculate_fibonacci():
    try:
        n = int(entry.get())
        result = fibonacci(n)
        result_label.config(text=f"Fibonacci({n}) = {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

root = tk.Tk()
root.title("Fibonacci Calculator")
tk.Label(root, text="Enter a number:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
tk.Button(root, text="Calculate", command=calculate_fibonacci).pack(pady=10)
result_label = tk.Label(root, text="Fibonacci result will appear here.")
result_label.pack(pady=10)

print("Starting")
root.mainloop()
