from pathlib import Path
import os
import sys

from kinco_var import KincoVar
from kinco_parser import read_vars_file, parse_vars


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Nincs megadva könyvtár!")
        exit(1)

    project_folder = Path(args[1])
    if not project_folder.is_dir():
        print("Helytelen könyvtár!")
        exit(1)


    # Változókat tartalmazó fájl keresése
    vars_file = None
    vars_file_type = "kgv"
    for file in os.listdir(project_folder):
        file_type = file.split(".")[-1].strip().lower()
        if file_type == vars_file_type:
            vars_file = os.path.join(project_folder, file)


    if vars_file is None:
        print(f"Nem található a változókat tartalmazó fájl ({vars_file_type} végződésű)!")
        exit(1)

    try: 
        content = read_vars_file(vars_file)
        variables = parse_vars(content)
        
        for var in variables:
            print(var)

    except:
        print("Probléma a fájl olvasása során!")
        exit(1)
