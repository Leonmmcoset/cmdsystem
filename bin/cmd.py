'''
 ██████╗███╗   ███╗██████╗      ██████╗ ██████╗ ███╗   ██╗███████╗ ██████╗ ██╗     ███████╗
██╔════╝████╗ ████║██╔══██╗    ██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██║     ██╔════╝
██║     ██╔████╔██║██║  ██║    ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     █████╗
██║     ██║╚██╔╝██║██║  ██║    ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██╔══╝
╚██████╗██║ ╚═╝ ██║██████╔╝    ╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗███████╗
 ╚═════╝╚═╝     ╚═╝╚═════╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝

CMD System by LeonMMcoset
(C)LeonMMcoset 2021-2024.All rights reserved.
Use Python
'''
#System start
print('///---CORE SYSTEM---///')
print('FOR CMD SYSTEM RUNNING CORE')
print('CORE IS CODE BY LEONMMCOSET')
print('COPYRIGHT LEONMMCOSET 2021-2024.ALL RIGHTS RESERVED.')
print('-----------------------')
print('CORE LOADING...')
SYSTEMCLOSE = ''
from time import *
from leonranp import *
from system import prosess as p
from PIL import Image
import os
from shutil import *
print('LOAD DONE.')
#Color must put here!
from system import color
while True:
    if SYSTEMCLOSE == True:
        break
    print('---Choose system start up mode---')
    print('1.Normal')
    print('2.Shutdown')
    SYSTEMCHOOSEMODE = input('Mode:')
    if SYSTEMCHOOSEMODE == '2':
        from system import audio as au
        break
    elif SYSTEMCHOOSEMODE == '1':
        #SYSTEM APPCATION LIST START
        print(color.green+'Starting...'+color.end)
        p.setbar(3)
        from app import cal
        from app import calnew
        from app import codex
        from app import echo
        from app import game
        from app import picsee
        from app import test
        from app import version
        from app import web
        from app import dead
        from app import file
        from app import runpy
        from app import music
        from app import video
        from app import vbs
        from app import blockgame as bg
        from app import downloader
        from app import pip
        from app import outside_app_docx as osappdocx
        from app import outside_app_installer as osappins
        p.bar()
        print(color.blue+'[SYSTEM]Local appcation load done'+color.end)
        from windows import cmd
        from windows import winver
        from windows import shutdown
        p.bar()
        print(color.blue+'[SYSTEM]Windows appcation load done'+color.end)
        from system import death
        from system import time
        from system import color
        from system import user
        from system import audio as au
        from system import app as outapp
        from system import localdownloader as ldown
        from system import config
        p.bar()
        print(color.blue+'[SYSTEM]System config load done'+color.end)
        #Check "pygame" folder,need pygame!
        # if not os.path.isdir('C:\cmd/conf'):
        #     os.mkdir('C:\cmd')
        #     os.mkdir('C:\cmd\conf')
        # if not os.path.isfile('C:\cmd\conf\main.properties'):
        #     copyfile('_internal/cmd/conf\main.properties', 'C:\cmd\conf')
        # os.chmod('C:\cmd\conf\main.properties', 0o666)
        config.running()
        if not os.path.isdir('C:\cmd\outapp\pygame'):
            print('Please wait!Don\'t close the appcation!')
            rmtree('C:\cmd\outapp')
            ldown.copy_file('_internal\\cmd\\outapp','C:\\cmd\\outapp')
        #Config load start#
        if config.main('test'):
            print('Test conf done!')
        else:
            pass
        #Config load end#
        if config.main('image'):
            image = Image.open('_internal/image/icon.png')
            new_width, new_height = image.size
            new_width //= 4
            new_height //= 4
            image = image.resize((new_width, new_height))

            # 转换图像为灰度模式
            image = image.convert("L")

            # 获取图像的像素值
            pixels = list(image.getdata())

            # 字符映射
            char_map = " .:-=+*#"  # 7个字符

            # 将像素值转换为字符表示，并打印到控制台
            for i in range(new_height):
                for j in range(new_width):
                    pixel_value = pixels[i * new_width + j]
                    # 将像素值映射到字符
                    char_index = int(pixel_value / 36)  # 将0-255的灰度值映射到0-6之间
                    if char_index >= len(char_map):
                        char_index = len(char_map) - 1
                    char = char_map[char_index]
                    print(char, end="")
                print()  # 换行
        print('-------------------------------------------')
        print('CMD system made by LeonMMcoset')
        print('(C)LeonMMcoset 2021-2024')
        time.time()
        print('-------------------------------------------')
        au.playaudio('_internal/audio/startup.mp3')
        user.start()
        au.playaudio('_internal/audio/login.mp3')
        #SYSTEM APPCATION LIST END
        #Command
        while True:
            com = input(color.blue+'System $'+color.end)
            try:
                if com == 'version':
                    version.start()
                elif com == 'test':
                    test.start()
                elif com == 'cal':
                    cal.start()
                elif com == 'calnew':
                    calnew.start()
                elif com =='exit' or com =='stop':
                    SYSTEMCLOSE = True
                    break
                elif com =='winver':
                    winver.start()
                elif com =='echo':
                    echo.start()
                elif com =='codex':
                    codex.start()
                elif com =='game':
                    game.start()
                elif com =='random':
                    sample()
                elif com =='cmd':
                    cmd.start()
                elif com =='picsee':
                    picsee.start()
                elif com =='web':
                    web.start()
                elif com =='dead':
                    dead.start()
                elif com =='time':
                    time.time()
                elif com =='file':
                    file.start()
                elif com =='runpy':
                    runpy.start()
                elif com =='music':
                    music.start()
                elif com =='video':
                    video.start()
                elif com =='color':
                    color.start()
                elif com =='':
                    pass
                elif com =='vbs':
                    vbs.start()
                elif com =='blockgame':
                    bg.start()
                    print('To exit,use Alt+F4 or ESC.')
                elif com =='downloader':
                    downloader.start()
                elif com =='shutdown':
                    shutdown.shutdown()
                elif com =='restart':
                    shutdown.restart()
                elif com =='sleep':
                    shutdown.sleep()
                elif com =='pip':
                    pip.start()
                elif com =='app docx':
                    osappdocx.start()
                elif com =='app':
                    outapp.start()
                elif com =='app install':
                    osappins.start()
                elif com =='config':
                    config.start()
                else:
                    print(color.red+'Error:"',com,'"is not a command!'+color.end)
            except Exception as ecpt:
                death.dead(1,ecpt)
    else:
        print(color.red+'Choose failed!'+color.end)
        from system import audio as au
print(color.green+'Shutdown...'+color.end)
au.playaudio('_internal/audio/shutdown.mp3')
sleep(1)