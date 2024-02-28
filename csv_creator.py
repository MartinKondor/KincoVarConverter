"""
Example export:

"AddrTag Lib"	"V116"
"AddrTagName"	"AddrHMIID"	"AddrPLCID"	"DataType"	"AddrType"	"Addr"	"AddrCodeType"	"AddrTypeName"	"AddrTagDataType"	"EnableAddrTagDataType"	"Description"	
"New Tag (noname0)"	"0"	"0"	"0"	"254"	"0"	"0"	"LB"	0	0
"""
from typing import List

from kinco_var import KincoVar


def create_csv(vars: List[KincoVar]) -> bool:
    """
    :returns: True if the save is successfull False otherwise
    """
    return False
