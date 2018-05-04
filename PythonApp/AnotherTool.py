import subprocess

from InstallOrExecute import InstallOrExecute


class AnotherTool:
    # a class that is meant to execute any othor tool except for F-Scure tool
    def __init__(self, fs_path, another_path):
        self.fs_path = fs_path
        self.another_path = another_path
        self.execute_tool = InstallOrExecute(self.another_path)

    def execute_another_tool(self):
        while True:

            if self.another_path == self.fs_path or not self.another_path:
                print("Error! Please provide another path!")
                break
            elif self.another_path != self.fs_path:
                self.execute_tool.install_execute_program()
                break
            else:
                break


