import os
os.system(f'git add .')
os.system(f'git commit -m "Normal update"')
# os.system(f'git pull --rebase origin main')
os.system(f'git pull origin main')
os.system(f'git push -u origin main')
os.system(f'pyinstaller --add-data "venv/bin/_internal/audio:audio"\
          --add-data "venv/bin/_internal/font:font"\
          --add-data "venv/bin/_internal/image:image"\
          --add-data "venv/bin/_internal/docx:docx"\
          --add-data "venv/bin/_internal/app:app"\
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
          --collect-submodules panda3d --collect-binaries panda3d --collect-data panda3d --collect-data ursina --collect-submodules ursina --collect-binaries ursina --collect-data panda3d-1.10.14.dist-info --collect-submodules panda3d-1.10.14.dist-info --collect-binaries panda3d-1.10.14.dist-info --collect-data ursina-7.0.0.dist-info --collect-submodules ursina-7.0.0.dist-info --collect-binaries ursina-7.0.0.dist-info\
          -i="C:\\Users\\leonm\\PycharmProjects\\leonsystem\\icon.ico" \
          -D -y \
          C:\\Users\leonm\PycharmProjects\leonsystem\\venv\\bin\cmd.py')
#Just do something I wanna to do.
#-----RENDER-----#
