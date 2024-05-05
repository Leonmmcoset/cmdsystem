#Outside Appcation Docx#
import os
import webbrowser

def start():
    def open_html_file(file_path):
        """打开本地HTML文件"""
        # 获取文件的绝对路径
        abs_path = os.path.abspath(file_path)

        # 构建文件的URL
        file_url = 'file://' + abs_path

        # 使用默认的浏览器打开URL
        webbrowser.open(file_url)


    def main():
        # HTML文件路径
        html_file_path = "_internal/docx/index.html"

        # 打开HTML文件
        open_html_file(html_file_path)


    main()
