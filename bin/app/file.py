import os
import subprocess
def start():
    def show_files_and_directories(path):
        # 获取当前路径下的所有文件和子目录
        files_and_dirs = os.listdir(path)

        # 遍历文件和子目录
        for item in files_and_dirs:
            item_path = os.path.join(path, item)

            # 判断是文件还是目录
            if os.path.isfile(item_path):
                print("File:", item)
            elif os.path.isdir(item_path):
                print("Directory:", item)


    def main():
        # 初始化，显示当前目录下的文件和子目录
        current_path = os.getcwd()
        print("Current Directory:", current_path)
        show_files_and_directories(current_path)

        # 循环，等待用户输入
        while True:
            choice = input(
                "\nEnter directory to navigate, 'open <filename>' to open a file, 'delete <filename>' to delete a file, or 'exit' to quit: ")

            # 如果用户输入了exit，则退出循环
            if choice.lower() == "exit":
                print("Exiting...")
                break

            # 如果用户想要打开文件
            elif choice.lower().startswith("open "):
                filename = choice.split(" ", 1)[1]
                file_path = os.path.join(current_path, filename)

                if os.path.exists(file_path) and os.path.isfile(file_path):
                    try:
                        subprocess.Popen([file_path], shell=True)
                    except Exception as e:
                        print("Error:", e)
                else:
                    print("File not found or invalid. Please try again.")

            # 如果用户想要删除文件
            elif choice.lower().startswith("delete "):
                filename = choice.split(" ", 1)[1]
                file_path = os.path.join(current_path, filename)

                if os.path.exists(file_path) and os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print("File", filename, "deleted successfully.")
                    except Exception as e:
                        print("Error:", e)
                else:
                    print("File not found or invalid. Please try again.")

            # 拼接用户输入的路径
            else:
                new_path = os.path.join(current_path, choice)

                # 检查路径是否存在并且是一个目录
                if os.path.exists(new_path) and os.path.isdir(new_path):
                    current_path = new_path
                    print("\nCurrent Directory:", current_path)
                    show_files_and_directories(current_path)
                else:
                    print("Invalid directory. Please try again.")


    main()
