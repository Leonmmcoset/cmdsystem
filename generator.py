#The Upload & Generator File#
import os
import shutil
try:
    shutil.rmtree('C:\\Users\leonm\PycharmProjects\leonsystem\\bin\_internal\cmd\outapp')
    os.mkdir('C:\\Users\leonm\PycharmProjects\leonsystem\\bin\_internal\cmd\outapp')
    shutil.copytree('C:\\Users\leonm\AppData\Local\JetBrains\PyCharm2023.2\python_stubs\\45802391','C:\\Users\leonm\PycharmProjects\leonsystem\\bin\_internal\cmd\outapp')
except:
    pass
shutil.copytree('C:\\Users\leonm\PycharmProjects\leonsystem\\bin\system','C:\\Users\leonm\PycharmProjects\leonsystem\\bin\_internal\cmd\outapp\system')
os.system(f'pyinstaller --add-data "bin/_internal/audio:audio"\
          --add-data "bin/_internal/font:font"\
          --add-data "bin/_internal/image:image"\
          --add-data "bin/_internal/cmd:cmd"\
          --add-data "C:\\Users\\leonm\PycharmProjects\leonsystem\\venv\Lib\site-packages\\ursina:usina/"\
          --add-data "C:\\Users\\leonm\PycharmProjects\leonsystem\\venv\Lib\site-packages\\ursina-7.0.0.dist-info:ursina-7.0.0.dist-info"\
          --add-data "C:\\Users\leonm\PycharmProjects\leonsystem\\venv\Lib\site-packages\panda3d:panda3d"\
          --add-data "C:\\Users\\leonm\PycharmProjects\\leonsystem\\venv\Lib\site-packages\panda3d-1.10.14.dist-info:panda3d-1.10.14.dist-info"\
          --add-data "C:\\Users\leonm\PycharmProjects\leonsystem\\venv\Lib\site-packages\panda3d_tools:panda3d_tools"\
          --add-data "C:\\Users\leonm\PycharmProjects\leonsystem\\venv\Lib\site-packages\direct:direct"\
          --add-data "C:\\Users\leonm\PycharmProjects\leonsystem\\venv\Lib\site-packages\pipeline:pipeline"\
          --add-data "C:\\Users\leonm\PycharmProjects\leonsystem\\venv\Lib\site-packages\pipeline-0.1.0.dist-info:pipeline-0.1.0.dist-info"\
          --path "C:\\Users\leonm\PycharmProjects\leonsystem\\venv\Lib\site-packages\panda3d"\
          --path "C:\\Users\\leonm\PycharmProjects\leonsystem\\venv\Lib\site-packages\\ursina"\
          --path "C:\\Users\\leonm\PycharmProjects\leonsystem\\venv\Lib\site-packages\\ursina-7.0.0.dist-info"\
          --path "C:\\Users\\leonm\PycharmProjects\\leonsystem\\venv\Lib\site-packages\panda3d-1.10.14.dist-info"\
          --collect-submodules panda3d --collect-binaries panda3d --collect-data panda3d --collect-data ursina \
          -i="C:\\Users\\leonm\\PycharmProjects\\leonsystem\\icon.ico" \
          -D -y \
          C:\\Users\leonm\PycharmProjects\leonsystem\\bin\cmd.py')
#If you want to generate .py to .exe,delete code done below.
os.system(f'git add .')
os.system(f'git commit -m "Normal update"')
os.system(f'git pull origin main')
os.system(f'git push -u origin main')
#Just do something I wanna to do.