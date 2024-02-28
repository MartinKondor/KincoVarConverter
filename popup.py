import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

from language import SAVE_AS_EXPORT, CHOOSE_FOLDER


def ask_for_filename() -> str:
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.asksaveasfilename(
        title=SAVE_AS_EXPORT,
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        defaultextension=".csv"
    )
    root.destroy()
    return filename


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

def ask_for_path() -> str:
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title=CHOOSE_FOLDER)
    root.destroy()
    return directory
