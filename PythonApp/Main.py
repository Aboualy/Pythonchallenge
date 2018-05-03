from AnotherTool import AnotherTool
from Tool import Tool
from Server import Server

#to check whether a specific file exists on the desktop or not


def main():
    p_url = "ftp://ftp.f-secure.com/support/tools/fsdiag/fsdiag_standalone.exe"
    p_name = p_url.split('/')[-1]
    server = Server(p_url, p_name)
    server.download_save_program()
    tool_path = input("Please enter the path of the installed F-Secure tool (copy/paste ): ")
    tool = Tool(tool_path)
    tool.execute_fsecure_tool()
    tool.check_fsecure_existence()
    another_tool_path = input("Please enter a path of another tool/program to be executed (copy/paste ): ")
    another_tool = AnotherTool(tool_path, another_tool_path)
    another_tool.execute_another_tool()


if __name__ == "__main__":
    # execute only if run as a script
    main()


