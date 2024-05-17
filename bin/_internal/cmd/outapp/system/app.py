#Outside App Running System File#
###---BUG LIST NO.1---###
##Fix about 10 days bug!##
import os
import importlib.util
def start():
    def find_and_run_script(script_name):
        try:
            # 构建脚本文件的绝对路径
            script_path = os.path.abspath(os.path.join("C:\\cmd\\outapp\\", script_name + ".py"))

            # 确认脚本文件存在
            if os.path.exists(script_path):
                # 动态导入脚本
                spec = importlib.util.spec_from_file_location(script_name, script_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # 调用脚本的start()函数
                if hasattr(module, 'start'):
                    module.start()
                else:
                    print(f"Error: {script_name} does not contain a start() function.")
            else:
                print(f"Error: Script file {script_path} not found.")
        except Exception as e:
            # 捕获并打印异常信息
            print(f"An error occurred while running script {script_name}: {e}")

    def startapp():
        script_name = input("Enter the script name to run: ")
        find_and_run_script(script_name)

    startapp()
