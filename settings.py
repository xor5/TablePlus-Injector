from tkinter import Tk, filedialog
import os

global dirpath

def open_folder_cli():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    folder_path = filedialog.askdirectory(
        title="Select installation folder"
    )

    root.destroy()

    if not folder_path:
        raise RuntimeError("No folder selected")

    return folder_path

def settings():
    global dirpath
    settings_path = 'settings.txt'
    if not os.path.exists(settings_path):
        folder_path = open_folder_cli()
        with open(settings_path, 'w') as f:
            f.write("targetpath=" + os.path.join(folder_path, "TablePlus.exe"))
            dirpath = folder_path
    else:
        with open(settings_path, 'r') as f:
            lines = f.readlines()
        dirpath = ""
        for line in lines:
            if line.startswith("targetpath="):
                dirpath = line.split("=", 1)[1].strip()
        if not dirpath or not os.path.exists(dirpath):
            dirpath = open_folder_cli()
            with open(settings_path, 'w') as f:
                f.write("targetpath=" + os.path.join(dirpath, "TablePlus.exe"))
    return dirpath