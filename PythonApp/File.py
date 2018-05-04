import os
import subprocess


class File:
    # A class that is meant to check if the file fsdiag.7z exists on the user´s desktop

    @staticmethod
    def check_fsecure_file_existence():
        try:
            file = os.path.expanduser("~/Desktop/fsdiag.7z")
            #A test with a text file on my desktop and it works
            #file = os.path.expanduser("~/Desktop/txt.txt")
        except IOError:
            file = False
        if os.path.isfile(file):
            print("The file exists on your desktop")
        else:
            print("The file doesn't exist on your desktop")
