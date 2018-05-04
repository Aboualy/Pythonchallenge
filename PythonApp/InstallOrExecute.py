import codecs
import os
import subprocess


class InstallOrExecute:
    def __init__(self, program):
        self.program = program

    def install_execute_program(self):
    #subprocess.check_call(self.program_name, shell=True)
        with codecs.open(os.devnull, 'wb', encoding='utf8') as std:
                subprocess.Popen(self.program,
                                      stdout=std,
                                      shell=True,
                                      stderr=subprocess.STDOUT
                                      )