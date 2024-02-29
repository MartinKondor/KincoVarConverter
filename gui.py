import tkinter as ttk
import customtkinter as tk  # https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22

from tkinter import filedialog, messagebox
from pathlib import Path
from typing import List
import os
from kinco_var import KincoVar
from kinco_parser import read_vars_file, parse_vars
from csv_creator import create_csv, save_csv
from language import (
    ERROR_NO_DIRECTORY,
    ERROR_INVALID_DIRECTORY,
    ERROR_FILE_NOT_FOUND,
    ERROR_FILE_READING,
    ERROR_CSV_EXPORT,
    SUCCESS_MSG,
    CHOOSE_FOLDER,
    SAVE_AS_EXPORT,
    GUI_TITLE,
    GUI_CHOOSE,
    GUI_CONVERT,
    HELP_BTN
)


class KincoPLCExporterApp:

    def __init__(self, root: tk.CTk):
        self.root = root
        self.root.title(GUI_TITLE)

        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.bind('<Key>', self.keypress)
        self.root.after(201, lambda: self.root.iconbitmap('icon.ico')) 

        FG_COLOR = "#f15b28"
        HOVER_COLOR = "#c74a20"
        default_font = tk.CTkFont(family="Arial", weight="bold")
        btn_base = {
            "fg_color": FG_COLOR,
            "hover_color": HOVER_COLOR,
            "text_color": "black",
            "font": default_font
        }

        self.project_folder_label = tk.CTkLabel(root, text=CHOOSE_FOLDER, font=default_font)
        self.project_folder_label.grid(row=0, column=1, padx=5, pady=5)

        self.project_folder_entry = tk.CTkEntry(root, width=400)
        self.project_folder_entry.grid(row=1, column=1, padx=5, pady=5)

        self.browse_button = tk.CTkButton(root, text=GUI_CHOOSE, command=self.browse_project_folder, **btn_base)
        self.browse_button.grid(row=1, column=2, padx=5, pady=5)

        self.export_button = tk.CTkButton(root, text=GUI_CONVERT, command=self.export_variables, **btn_base)
        self.export_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def browse_project_folder(self):
        folder_path = filedialog.askdirectory(title=CHOOSE_FOLDER)
        if folder_path:
            self.project_folder_entry.delete(0, tk.END)
            self.project_folder_entry.insert(0, folder_path)

    def export_variables(self):
        project_folder = self.project_folder_entry.get()

        if not project_folder:
            messagebox.showerror("Error", ERROR_NO_DIRECTORY)
            return

        project_folder = Path(project_folder)
        if not project_folder.is_dir():
            messagebox.showerror("Error", ERROR_INVALID_DIRECTORY)
            return

        vars_file = None
        vars_file_type = "kgv"
        for file in os.listdir(project_folder):
            file_type = file.split(".")[-1].strip().lower()
            if file_type == vars_file_type:
                vars_file = os.path.join(project_folder, file)
                break

        if vars_file is None:
            messagebox.showerror("Error", ERROR_FILE_NOT_FOUND.format(file_type=vars_file_type))
            return

        try:
            content = read_vars_file(vars_file)
            variables: List[KincoVar] = parse_vars(content)

            try:
                csv_contents = create_csv(variables)
                filename = filedialog.asksaveasfilename(
                    title=SAVE_AS_EXPORT,
                    defaultextension=".csv",
                    filetypes=[
                        ("CSV Files", "*.csv")
                    ]
                )

                if filename:
                    save_csv(filename, csv_contents)
                    messagebox.showinfo("Success", SUCCESS_MSG.format(filename=filename))

            except Exception as e:
                messagebox.showerror("Error", ERROR_CSV_EXPORT)
                print(e)

        except Exception as e:
            messagebox.showerror("Error", ERROR_FILE_READING)
            print(e)

    def keypress(self, event):
        #print(repr(event.char))
        pass

    def on_closing(self):
        self.root.destroy()


def main():
    tk.set_appearance_mode("dark")
    root = tk.CTk()
    app = KincoPLCExporterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
