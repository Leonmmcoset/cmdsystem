import shutil

def copy_file(source_path, destination_path):
    try:
        # 复制文件
        shutil.copytree(source_path, destination_path)
    except Exception as e:
        raise OSError(f"An error occurred while copying file: {e}")