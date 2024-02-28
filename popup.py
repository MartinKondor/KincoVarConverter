import tkinter as tk
from tkinter import messagebox


def show_error_popup(message: str) -> None:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", message)
    root.destroy()


def show_popup(message: str) -> None:
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Info", message)
    root.destroy()
