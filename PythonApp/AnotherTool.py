import subprocess


class AnotherTool:
    def __init__(self, fs_path, another_path):
        self.fs_path = fs_path
        self.another_path = another_path

    def execute_another_tool(self):
        while True:

            if self.another_path == self.fs_path or not self.another_path:
                print("Error! Please provide another path!")
                break
            elif self.another_path != self.fs_path:
                subprocess.check_call(self.another_path)
                break
            else:
                break


