import os
import requests
from urllib.parse import urlparse
import subprocess
from system import *
def start():
    def installer():
        print('---Install App---')
        print('1.App Store')
        print('2.URL')
        insmode = int(input('Choose mode:'))
        if insmode == 1:
            print('Store link:https://cmdstore.netlify.app')
            def install(url, save_dir):
                # 发送GET请求下载文件
                response = requests.get(url)
                # 获取文件名
                parsed_url = urlparse(url)
                file_name = os.path.basename(parsed_url.path)
                # 构建保存路径
                save_path = os.path.join(save_dir, file_name)
                # 写入文件
                print(color.blue + '[DOWNLOADER]Please wait...' + color.end)
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                print(color.green + "Download done!" + color.end)
            save_dir = "_internal//outapp"
            appurl = "https://cmdstore.netlify.app/app/"
            insappname = appurl + input('App name:') + '.py'
            install(insappname,save_dir)

        elif insmode == 2:
            def download_file(url, save_dir):
                # 发送GET请求下载文件
                response = requests.get(url)
                # 获取文件名
                parsed_url = urlparse(url)
                file_name = os.path.basename(parsed_url.path)
                # 构建保存路径
                save_path = os.path.join(save_dir, file_name)
                # 写入文件
                print(color.blue + '[DOWNLOADER]Please wait...' + color.end)
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                print(color.green + "Download done!" + color.end)

            def main():
                url = input("Download link:")
                save_dir = "_internal//outapp"

                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                download_file(url, save_dir)

            main()
        else:
            print(color.red+'Choose failed!'+color.end)
    installer()