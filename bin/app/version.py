#Command system version
#/outapp/version
from system import time
def start():
    import platform
    import subprocess
    import psutil

    # 检测Windows版本
    windows_version = platform.platform()

    # 获取CMD名称
    processor_info = platform.processor()

    # 获取RAM信息
    ram_info = psutil.virtual_memory()
    ram_total = ram_info.total
    ram_total_gb = ram_total / (1024 ** 3)  # 将字节转换为GB
    print('-------------------------------------------')
    print('CMD Console')
    print('Coded by LeonMMcoset')
    print('(C)LeonMMcoset 2021-2024')
    print('Version 30 New Picsee')
    print('Windows version:',windows_version)
    print('Processor:',processor_info)
    print('RAM:',ram_total,'B')
    print('-------------------------------------------')