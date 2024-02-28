from typing import List

from kinco_var import KincoVar


def read_vars_file(vars_file: str) -> str:
    """
    :returns: str with the file's contents
    """
    file = open(vars_file, "r")
    contents = file.read()
    file.close()
    return contents


def parse_line(line: str) -> KincoVar:
    """
    Example_
    >>> line = "O_G2_elszivo AT  %Q0.3    :BOOL  ;  (*comment*)"
    >>> parse_line(line)
    {
        "name": "O_G2_elszivo",
        "address": "%Q0.3",
        "type": "bool",
        "comment": "comment"
    }
    """
    parts = line.split(':')

    name_address_part = parts[0].split('AT')
    name = name_address_part[0].strip()
    address = name_address_part[1].strip()

    var_type = parts[1].split(';')[0].strip().lower()
    comment = parts[1].split(';')[1].strip()[2:-2].strip() if len(parts) > 1 and ';' in parts[1] else ""
    return KincoVar(name, address, var_type, comment)


def parse_vars(vars_content: str) -> List[KincoVar]:
    variables = []
    lines = vars_content.splitlines()
    can_parse = False

    for i, line in enumerate(lines):
        clean_line = line.strip().lower()
        if clean_line == "var_global":
            can_parse = True
            continue
        if clean_line == "end_var":
            can_parse = False
            break

        if can_parse is not True:
            continue

        line = line.strip()
        variables.append(parse_line(line))

    return variables
