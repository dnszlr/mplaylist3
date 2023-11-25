import logging
from file_handling import is_exe

def info(message):
    if is_exe():
        logging.info(message)
    else:
        print(f"Info: {message}")

def debug(message):
    if is_exe():
        logging.debug(message)
    else:
        print(f"Debug: {message}")        

def error(message):
    if is_exe():
        logging.error(message)
    else:
        print(f"Error: {message}")


def configureDebug(filename):
    configureLogger(filename, logging.debug)

def configureInfo(filename):
    configureLogger(filename, logging.INFO)
    
def configureLogger(filename, level):
    logging.basicConfig(
        filename=filename, 
        level=level, 
        format='%(asctime)s [%(levelname)s]: %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S')