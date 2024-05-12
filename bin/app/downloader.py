import requests
import subprocess
import os
from system import *
from urllib.parse import urlparse
def start():

    def download_file(url, save_dir):
        print(color.blue+'[DOWNLOADER]Please wait...'+color.end)
        versio# 发送GET请求下载文件
        response = requests.get(url)
        # 获取文件名
        parsed_url = urlparse(url)
        file_name = os.path.basename(parsed_url.path)
        # 构建保存路径
        save_path = os.path.join(save_dir, file_name)
        # 写入文件

        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(color.green+"Download done!"+color.end)
        return save_path

    def run_file(file_path):
        # 使用subprocess运行文件
        subprocess.Popen([file_path], shell=True)

    def main():
        url = input("Download link:")
        save_dir = input("Download path:")

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        file_path = download_file(url, save_dir)

        # 询问用户是否要自动运行
        auto_run = input(color.green+"File download done!"+color.end+"Run?(yes/no): ").lower()

        if auto_run == 'yes':
            run_file(file_path)

    main()