from pathlib import Path
from typing import List
from sys import exit
import os
import sys

from kinco_var import KincoVar
from kinco_parser import read_vars_file, parse_vars
from language import (
    ERROR_NO_DIRECTORY,
    ERROR_INVALID_DIRECTORY,
    ERROR_FILE_NOT_FOUND,
    ERROR_FILE_READING,
    ERROR_CSV_EXPORT,
    SUCCESS_MSG
)
from popup import show_error_popup, show_popup, ask_for_filename, ask_for_path
from csv_creator import create_csv, save_csv


if __name__ == "__main__":
    args = sys.argv
    project_folder = None
    is_debug_mode = False

    if len(args) == 3:
        if args[-1] == "debug":
            is_debug_mode = True
            show_error_popup = print
            show_popup = print

    if len(args) < 2:
        #show_error_popup(ERROR_NO_DIRECTORY)
        #exit(1)
        project_folder = ask_for_path()
        if project_folder is None or project_folder == "":
            exit(0)
    else:
        project_folder = args[1]

    project_folder = Path(project_folder)
    if not project_folder.is_dir():
        show_error_popup(ERROR_INVALID_DIRECTORY)
        exit(1)


    # Változókat tartalmazó fájl keresése
    vars_file = None
    vars_file_type = "kgv"
    for file in os.listdir(project_folder):
        file_type = file.split(".")[-1].strip().lower()
        if file_type == vars_file_type:
            vars_file = os.path.join(project_folder, file)


    if vars_file is None:
        show_error_popup(ERROR_FILE_NOT_FOUND.format(file_type=vars_file_type))
        exit(1)

    try: 
        content: str = read_vars_file(vars_file)
        variables: List[KincoVar] = parse_vars(content)
        
        try:
            csv_contents = create_csv(variables)
            filename = ask_for_filename()
            
            if filename:
                save_csv(filename, csv_contents)
                show_popup(SUCCESS_MSG.format(filename=filename))
        
        except Exception as e:
            if is_debug_mode:
                raise e
            show_error_popup(ERROR_CSV_EXPORT)

    except Exception as e:
        if is_debug_mode:
            raise e
        show_error_popup(ERROR_FILE_READING)
