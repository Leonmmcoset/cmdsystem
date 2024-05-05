import subprocess
import sys
def start():
    def check_pip():
        """检查是否安装了pip"""
        try:
            # 尝试导入pip模块
            import pip
            return True
        except ImportError:
            return False

    def install_package(package_name):
        """使用pip安装包"""
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
            print(f"Package '{package_name}' installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to install package '{package_name}'.")

    def main():
        if check_pip():
            print("pip is installed on your system.")
            package_name = input("Enter the package name you want to install: ")
            install_package(package_name)
        else:
            print("pip is not installed on your system.")
            print("Please install pip first. You can download get-pip.py and run it using python.")
            print("Visit https://pip.pypa.io/en/stable/installing/ for instructions on installing pip.")

    main()