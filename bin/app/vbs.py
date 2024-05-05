def start():
    import subprocess

    def run_vbs_script(script_path):
        subprocess.run(["cscript.exe", script_path], check=True)
    vbs_script_path = input("Please input VBS file's path: ")
    run_vbs_script(vbs_script_path)
