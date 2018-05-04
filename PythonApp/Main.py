from AnotherTool import AnotherTool
from InstallOrExecute import InstallOrExecute
from File import File
from Server import Server


def main():

    p_url = "ftp://ftp.f-secure.com/support/tools/fsdiag/fsdiag_standalone.exe"

    #Get the tool name out of the url
    p_name = p_url.split('/')[-1]

    #Creating an object of the class Server
    server = Server(p_url, p_name)

    #Saving the F-Secure tool into the same directory
    server.download_program()

    #install F-Secure tool
    in_f = InstallOrExecute(p_name).install_execute_program
    in_f()
    tool_path = input("Please enter the path of the installed F-Secure tool (copy/paste ):\n \n")

    #Execute F-Secure tool
    ex_f = InstallOrExecute(tool_path).install_execute_program
    ex_f()

    # Execute any tool other than F-Secure tool
    another_tool_path = input("Please enter a path of another tool/program to be executed (copy/paste ):\n\n")
    another_tool = AnotherTool(tool_path, another_tool_path).execute_another_tool
    another_tool()

    #Chech whether fsdiag.7z exists on the user desktop or not
    f = File.check_fsecure_file_existence
    f()

if __name__ == "__main__":
    # execute only if run as a script
    main()


