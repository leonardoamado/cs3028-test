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
root.geometry("300x300")

tk.Label(root, text="Enter a number:", font=("Arial", 14)).pack(pady=20)  # Larger label with padding
entry = tk.Entry(root, width=30, font=("Arial", 12))  # Wider entry box with larger font
entry.pack(pady=10)
tk.Button(root, text="Calculate", command=calculate_fibonacci, width=15, height=2, font=("Arial", 12)).pack(pady=20)
result_label = tk.Label(root, text="Fibonacci result will appear here.", font=("Arial", 14), width=40, height=2)
result_label.pack(pady=20)

print("Starting")
root.mainloop()
