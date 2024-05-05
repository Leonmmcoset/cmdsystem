def start():
    import subprocess
    import os


    def run_python_script(script_path):
        # 确保文件存在并且是一个Python脚本
        if not os.path.exists(script_path):
            print(f"Error: File '{script_path}' does not exist.")
            return
        if not script_path.endswith('.py'):
            print(f"Error: '{script_path}' is not a Python script.")
            return

        # 使用subprocess运行Python脚本
        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True)
            if result.returncode == 0:
                print("Script ran successfully.")
                print("Output:\n", result.stdout)
            else:
                print("Script failed with return code:", result.returncode)
                print("Error output:\n", result.stderr)
        except Exception as e:
            print("An error occurred:", e)


    # 示例：运行一个Python脚本
    script_to_run = input("Enter the path to the Python script you want to run: ")
    run_python_script(script_to_run)
