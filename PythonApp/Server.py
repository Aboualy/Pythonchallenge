import codecs
import os
import shutil
import subprocess
import urllib
import urllib.request
#a class that is meant to download F-Scure tool
class Server:
    def __init__(self, program_url, program_name):
        self.program_url = program_url
        self.program_name = program_name

    def download_program(self):
        with urllib.request.urlopen(self.program_url) as req, open(self.program_name, 'wb') as result:
            shutil.copyfileobj(req, result)

