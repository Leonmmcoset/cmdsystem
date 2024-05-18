#Config Loading File
#Load system conf file
import os
import shutil
from system import color
def main(variable_to_check):
    try:
        os.chmod('C:\cmd\conf\main.properties', 0o666)
        with open('C:\cmd\conf\main.properties', 'r') as file:
            for line in file:
                # 忽略以 '#' 开头的行和空行
                if line.startswith('#') or not line.strip():
                    continue
                # 去除行尾的换行符并分割出变量名和值
                variable, value = line.strip().split(' = ')
                # 如果找到要检查的变量名
                if variable == variable_to_check:
                    return value.strip() == 'True'
    except FileNotFoundError:
        print(f"File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False  # 如果未找到变量或发生异常，则默认返回 False
def running():
    if not os.path.isdir('C:\cmd/conf'):
        os.mkdir('C:\cmd')
        os.mkdir('C:\cmd\conf')
    if not os.path.isfile('C:\cmd\conf\main.properties'):
        shutil.copy('_internal/cmd/conf\main.properties', 'C:\cmd\conf')
    os.chmod('C:\cmd\conf\main.properties', 0o666)
def start():
    print('1.main')
    configchoose = input('Please choose section:')
    if configchoose == '1':
        print('test -> Test config running.')
        print('image -> See text-image.')
        # print('')
    else:
        print(color.red+'Choose failed!'+color.end)