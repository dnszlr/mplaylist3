import os, sys

def get_root_folder():
    path = os.path.abspath(__file__)
    if is_exe():
        path = sys.executable
    rootFolder = os.path.dirname(path)
    return rootFolder

def is_exe():
    is_exe = getattr(sys, 'frozen', False)
    return is_exe