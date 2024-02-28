from pathlib import Path
from typing import List
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
from popup import show_error_popup, show_popup
from csv_creator import create_csv


if __name__ == "__main__":
    args = sys.argv
    is_debug_mode = False

    if len(args) == 3:
        if args[-1] == "debug":
            is_debug_mode = True
            show_error_popup = print
            show_popup = print

    if len(args) < 2:
        show_error_popup(ERROR_NO_DIRECTORY)
        exit(1)

    project_folder = Path(args[1])
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
        is_success = create_csv(variables)
        
        if not is_success:
            show_error_popup(ERROR_CSV_EXPORT)
        else:
            show_popup(SUCCESS_MSG)
    except:
        show_error_popup(ERROR_FILE_READING)
        exit(1)
