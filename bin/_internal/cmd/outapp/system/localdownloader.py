import shutil

def copy_file(source_path, destination_path):
    try:
        # 复制文件
        shutil.copytree(source_path, destination_path)
        print(f"File copied successfully from {source_path} to {destination_path}")
    except Exception as e:
        print(f"An error occurred while copying file: {e}")