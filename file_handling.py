import os, sys

def get_root_folder():
    path = os.path.abspath(__file__)
    if is_exe:
        path = sys.executable
    return os.path.dirname(path)

def is_exe():
    return getattr(sys, 'frozen', False)