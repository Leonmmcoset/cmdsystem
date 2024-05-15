#Outside App Running System File#
###---BUG LIST NO.1---###
##Fix about 10 days bug!##
import os
import subprocess
import importlib

def start():
    import os
    import importlib.util

    def find_and_run_script(script_name):
        # 获取当前脚本所在目录的绝对路径
        current_dir = os.path.abspath(os.path.dirname(__file__))
        # 构建脚本文件的绝对路径
        script_path = os.path.join(current_dir, "..", "_internal", "outapp", script_name + '.py')
        print('Script path:' + script_path)
        try:
            # 尝试动态导入脚本
            spec = importlib.util.spec_from_file_location(script_name, script_path)
            script_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(script_module)
            # 如果脚本中有 start() 函数，则调用它
            if hasattr(script_module, 'start'):
                script_module.start()
            else:
                print(f"Error: {script_name} does not contain a start() function.")
        except Exception as e:
            # 捕获并打印异常信息
            print(f"An error occurred while running {script_name}: {e}")

    def startapp():
        script_name = input("Enter the script name to run: ")
        find_and_run_script(script_name)

    startapp()
