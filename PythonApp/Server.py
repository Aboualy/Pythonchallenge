import codecs
import os
import shutil
import subprocess
import urllib
import urllib.request


class Server:
    def __init__(self, program_url, program_name):
        self.program_url = program_url
        self.program_name = program_name

    def download_save_program(self):
        with urllib.request.urlopen(self.program_url) as req, open(self.program_name, 'wb') as result:
            shutil.copyfileobj(req, result)
        self.install_program()

    def install_program(self):
        subprocess.check_call(self.program_name, shell=True)