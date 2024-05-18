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
                line = line.strip()
                variable, value = line.split(' = ')
                value = value.strip()
                if variable == variable_to_check:
                    return value == 'True'
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