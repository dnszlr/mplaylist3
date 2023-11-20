import os, sys

def get_root_folder():
    path = os.path.abspath(__file__)
    if is_exe():
        print("is exe")
        path = sys.executable
    dire = os.path.dirname(path)
    return dire

def is_exe():
    return getattr(sys, 'frozen', False)