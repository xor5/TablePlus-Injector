from clear import clear
import os

def target_info():
    return {
        "CompanyName": "TablePlus, Inc",
        "FileDescription": "TablePlus",
        "FileVersion": "1.0",
        "LegalCopyright": "Copyright © 2026 TablePlus, Inc.                                                                    ",
        "OriginalFileName": "",
        "ProductName": "TablePlus",
        "ProductVersion": "6.8.1",
    }

def info_target():
    os.system("mode con cols=53 lines=30")
    os.system("title TBPLUS INJECTOR")
    clear()
    print("===================================================")
    length = 0
    for i, j in target_info().items():
        if i == "LegalCopyright":
            length = len(i.strip() + j.strip())
    for x, y in target_info().items():
        if x != "LegalCopyright":
            print("= " + x + ":" + y + ((length - len(x + y)) * " ") + " =")
        elif x == "LegalCopyright":
            print("= " + x + ":" + y)

    print("===================================================")

def info_injector():
    os.system("mode con cols=62 lines=30")
    os.system("title TBPLUS INJECTOR")
    clear()
    print("==============================================================")
    print("=              Inject TablePlus by FaizXor5                  =")
    print("=            GitHub: https://github.com/faiz3                =")
    print("==============================================================")
    print("=              This tool is for educational                  =")
    print("=                      purposes only.                        =")
    print("=                    LICENSE: MIT License                    =")
    print("= You are free to use, modify, and distribute this software. =")
    print("==============================================================")
    print("v1.0")