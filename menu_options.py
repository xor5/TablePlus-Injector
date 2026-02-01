from UpdateVersion import update
from infoapp import info_injector, info_target
from optioninfo import option_menu, option_info
from title import title_info
from inject import apply_patch, revert_patch
import sys
from settings import settings

def sub_menu():
    run = True
    while run:
        title_info()
        option_info()
        option = input("Select menu option: ")
        if option == "1":
            info_target()
        if option == "2":
            info_injector()
        if option == "9":
            run = False
        if option == "0":
            sys.exit(0)
        print("\nPress Enter for continue or Ctrl+C for exit code!")
        input()

def menu():
    option_menu()
    option = input("Select a menu option: ")
    if option == "1":
        update()
        print("\nPress Enter for continue or Ctrl+C for exit code!")
        input()
    if option == "2":
        apply_patch(settings())
    if option == "3":
        revert_patch(settings())
    if option == "9":
        sub_menu()
    if option == "0":
        sys.exit(0)

    return option
