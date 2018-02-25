from pathlib import Path
import os

"""Below mentioned functions are fundamental methods for file handing """
def check_file(path):
    if os.path.isfile(path):
        return True
    else:
        return False

def check_directory(path):
    if os.path.isdir(path):
        return True
    else:
        return False

def check_fileformat(path):
    spath = str(path).split("/")
    fformat = spath[-1].split(".")[-1]
    return fformat

def readfile_list(path):
    contents = []
    try:
        with open(path) as file_object:
            contents = file_object.readlines()
            return contents
    except FileNotFoundError:
        return ("File not found")

def filelist_toString(filelist):
    return filelist.