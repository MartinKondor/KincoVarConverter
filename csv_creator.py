"""
Example export:
vars = [
    {
        "name": "G1_Homerseklet",
        "address": "%AIW2",
        "type": "int",
        "comment": "Gépészet 1 hőmérséklet szenzor"
    },
    {
        "name": "O_G2_Hiba",
        "address": "%Q2.4",
        "type": "bool",
        "comment": ""
    },
    {
        "name": "M_G1_ELSZIVO_HIBA",
        "address": "%M5.3",
        "type": "bool",
        "comment": ""
    },
    {
        "name": "G1_Start",
        "address": "%I0.7",
        "type": "bool",
        "comment": ""
    },
    {
        "name": "G1_stop_utan_kesleltetes",
        "address": "%VW8",
        "type": "int",
        "comment": ""
    }
]

"AddrTag Lib"	"V116"
"AddrTagName"	"AddrHMIID"	"AddrPLCID"	"DataType"	"AddrType"	"Addr"	"AddrCodeType"	"AddrTypeName"	"AddrTagDataType"	"EnableAddrTagDataType"	"Description"	
"G1_Homerseklet"	"0"	"0"	"2"	"3"	"2"	"0"	"AIW"	0	0	Gépészet 1 hőmérséklet szenzor
"O_G2_Hiba"	"0"	"0"	"0"	"1"	"2.4"	"0"	"Q"	0	0	
"M_G1_ELSZIVO_HIBA"	"0"	"0"	"0"	"2"	"5.3"	"0"	"M"	0	0	
"G1_Start"	"0"	"0"	"0"	"0"	"0.7"	"0"	"I"	0	0	
"G1_stop_utan_kesleltetes"	"0"	"0"	"2"	"5"	"8"	"0"	"VW"	0	0	

Formatted example:
"AddrTag Lib"	"V116"
"AddrTagName"	    "AddrHMIID"	"AddrPLCID"	"DataType"	"AddrType"	"Addr"	"AddrCodeType"	"AddrTypeName"	"AddrTagDataType"	"EnableAddrTagDataType"	"Description"	
"G1_Homerseklet"    "0"	        "0"	        "2"	        "3"	        "2"	    "0"	            "AIW"	        0	                0	                    Gépészet 1 hőmérséklet szenzor
"O_G2_Hiba"	        "0"	        "0"	        "0"	        "1"	        "2.4"	"0"	            "Q"	            0	                0	
"M_G1_ELSZIVO_HIBA"	"0"	        "0"	        "0"	        "2"	        "5.3"	"0"	            "M"	            0                   0	
"G1_Start"	        "0"	        "0"	        "0"	        "0"	        "0.7"	"0"	            "I"	            0	                0
"G1_stop_utan_kesleltetes""0"	"0" 	    "2"	        "5"	        "8"	    "0"	            "VW"	        0	                0		
"Some_VR"	        "0"	        "0"	        "3"	        "9"	        "8"	    "0"	            "VR"	        0	                0	
"""
from typing import List
import shutil

from kinco_var import KincoVar


BASE_CSV = """
"AddrTag Lib"	"V116"
"AddrTagName"	"AddrHMIID"	"AddrPLCID"	"DataType"	"AddrType"	"Addr"	"AddrCodeType"	"AddrTypeName"	"AddrTagDataType"	"EnableAddrTagDataType"	"Description"
""".strip()


def determine_addr_type(addr_type_name: str) -> str:
    addr_type_name = addr_type_name.lower().strip()
    try:
        return {
            "iw": "0", "i": "0",
            "qw": "1", "q": "1",
            "mw": "2", "m": "2",
            "aiw": "3", "ai": "3",
            "vw": "5", "v": "5",
            "vr": "9",
        }[addr_type_name]
    except:
        return "0"


def determine_addr_values(addr_tag: str) -> List[str]:
    """
    :example input: "%AIW2", "%Q1.0"
    :returns: [addr_type_num, addr_type_name]
    """
    addr_tag = addr_tag[1:]
    clean_addr_tag = ""

    addr_type = "0"
    addr_code_type = "0"
    
    addr = ""
    addr_type_name = ""

    in_addr = True

    for ch in addr_tag:
        if ch.isnumeric():
            in_addr = False

        if in_addr:
            addr_type_name += ch
        if not in_addr:
            addr += ch

    addr_type = determine_addr_type(addr_type_name)

    # "AddrType"	"Addr"	"AddrCodeType"	"AddrTypeName"
    return addr_type, addr, addr_code_type, addr_type_name


def determine_data_type(var: KincoVar) -> str:
    if "VR" in var.address:
        return "3"
    return "2" if var.type == "int" else "0"


def create_csv(vars: List[KincoVar]) -> str:
    csv_contents = BASE_CSV
    newline = "\n"

    for var in vars:
        data_type = determine_data_type(var)
        addr_type, addr, addr_code_type, addr_type_name = determine_addr_values(var.address)

        if addr_type_name == "SM":
            continue

        csv_contents += f'"{var.name}"\t"0"\t"0"\t"{data_type}"\t"{addr_type}"\t"{addr}"\t"{addr_code_type}"\t"{addr_type_name}"\t0\t0\t{var.comment}{newline}'

    return csv_contents


def replace_hungarian_accents(text):
    accent_map = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ö': 'o', 'ő': 'o', 'ú': 'u', 'ü': 'u', 'ű': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ö': 'O', 'Ő': 'O', 'Ú': 'U', 'Ü': 'U', 'Ű': 'U'
    }
    translation_table = str.maketrans(accent_map)
    return text.translate(translation_table)


def save_csv(filename: str, csv_contents: str) -> None:
    shutil.copy("export_sample.csv", filename)
    with open(filename, "ab") as export_file:
        content_bytes = replace_hungarian_accents(csv_contents)\
            .encode("utf-16-le")\
            .replace(b"\r\n", b"\n")
        export_file.write(content_bytes)
    