#Outside App Running System File#
import os
import subprocess
import importlib

def start():
    def find_and_run_script(script_name):
        """查找并运行脚本"""
        # 获取 .internal/outapp 文件夹的路径
        script_dir = os.path.join("_internal", "outapp")

        # 构建脚本文件的绝对路径
        script_path = os.path.join(script_dir, script_name + ".py")

        # 检查文件是否存在
        if os.path.exists(script_path):
            # 动态导入脚本
            try:
                module = importlib.import_module(f"outapp.{script_name}", package="_internal")
                # 调用脚本中的 start() 函数
                module.start()
                return True
            except Exception as e:
                print('Error found! It is:', e)
                return False
        else:
            # 如果没有找到匹配的脚本
            print(f"No script named '{script_name}.py' found.")
            return False

    def startapp():
        """开始函数"""
        # 提示用户输入要运行的脚本名
        script_name = input("Enter the app name: ")

        # 查找并运行脚本
        find_and_run_script(script_name)

    startapp()
