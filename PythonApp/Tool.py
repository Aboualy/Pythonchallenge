import os
import subprocess


class Tool:
    def __init__(self, path):
        self.path = path

    def execute_fsecure_tool(self):
        subprocess.call(self.path)

    @staticmethod
    def check_fsecure_existence():
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
