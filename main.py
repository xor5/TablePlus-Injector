from title import title_app
from menu_options import menu
from permission import is_admin
import ctypes
import sys
import os
import signal

# terminal size & title
os.system("mode con cols=62 lines=30")
os.system("title TBPLUS INJECTOR")

def handle_exit(sig=None, frame=None):
    os._exit(0)

signal.signal(signal.SIGINT, handle_exit)

def start():
    if not is_admin():
        print("[!] Not running as administrator.")
        print("[*] Opening CMD as Administrator...")

        script = os.path.abspath(sys.argv[0])
        workdir = os.getcwd()

        cmd = f'/c cd /d "{workdir}" && "{sys.executable}" "{script}"'

        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            "cmd.exe",
            cmd,
            None,
            1
        )
        os._exit(0)

    title_app()
    menu()

def main():
    while True:
        start()

if __name__ == "__main__":
    main()
