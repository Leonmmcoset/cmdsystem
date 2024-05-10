#Outside App Running System File#
import os
import subprocess
import importlib

def start():
    def find_and_run_script(script_name):
        """查找并运行脚本"""
        # 获取 _internal/app/py 文件夹的路径
        script_dir = "_internal\app"

        # 遍历该文件夹中的所有文件
        for file_name in os.listdir(script_dir):
            # 如果文件名与输入的脚本名匹配
            if file_name == script_name + ".py":
                # 构建脚本文件的绝对路径
                script_path = os.path.join(script_dir, file_name)
                print('Script path:',script_path)
                # 动态导入脚本
                try:
                    module = importlib.import_module(f"app.{script_name}")
                    # 调用脚本中的 start() 函数
                    module.start()
                except ModuleNotFoundError:
                    print(f"Script '{script_name}' not found.")
                except AttributeError:
                    print(f"Script '{script_name}' does not have a 'start()' function.")

                return True

        # 如果没有找到匹配的脚本
        print(f"No script named '{script_name}.py' found.")
        return False


    def start():
        """开始函数"""
        # 提示用户输入要运行的脚本名
        script_name = input("Enter the app name: ")

        # 查找并运行脚本
        find_and_run_script(script_name)

    start()
