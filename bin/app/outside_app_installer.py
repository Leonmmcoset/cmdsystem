import os
import requests
from urllib.parse import urlparse
import subprocess
from system import *
def start():
    def installer():
        while True:
            print('---Install App---')
            print('1.App Store')
            print('2.URL')
            print('3.Exit')
            insmode = int(input('Choose mode:'))
            if insmode == 1:
                print('Store link:https://cmdstore.netlify.app')
                def install(url, save_dir):
                    print(color.blue + '[DOWNLOADER]Please wait...' + color.end)
                    # 发送GET请求下载文件
                    response = requests.get(url)
                    # 获取文件名
                    parsed_url = urlparse(url)
                    file_name = os.path.basename(parsed_url.path)
                    # 构建保存路径
                    save_path = os.path.join(save_dir, file_name)
                    # 写入文件

                    with open(save_path, 'wb') as f:
                        f.write(response.content)
                    print(color.green + "Download done!" + color.end)
                save_dir = "C:\\cmd\\outapp"
                appurl = "https://cmdstore.netlify.app/app/"
                insappname = appurl + input('App name:') + '.py'
                install(insappname,save_dir)

            elif insmode == 2:
                def download_file(url, save_dir):
                    print(color.blue + '[DOWNLOADER]Please wait...' + color.end)
                    # 发送GET请求下载文件
                    response = requests.get(url)
                    # 获取文件名
                    parsed_url = urlparse(url)
                    file_name = os.path.basename(parsed_url.path)
                    # 构建保存路径
                    save_path = os.path.join(save_dir, file_name)
                    # 写入文件

                    with open(save_path, 'wb') as f:
                        f.write(response.content)
                    print(color.green + "Download done!" + color.end)

                def main():
                    url = input("Download link:")
                    save_dir = "C:\\cmd\\outapp"

                    if not os.path.exists(save_dir):
                        os.makedirs(save_dir)
                    download_file(url, save_dir)

                main()
            elif insmode == 3:
                break
            else:
                print(color.red+'Choose failed!'+color.end)
    installer()