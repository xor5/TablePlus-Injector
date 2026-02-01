import os
import subprocess

def update():
    command =  'cd tbplus-injector && git pull'
    # open new terminal to run UpdateVersion.py
    if os.name == 'nt':  # Windows
        subprocess.Popen(['start', 'cmd', '/k', f'{command}'], shell=True)
    pass