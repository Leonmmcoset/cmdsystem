from ursina import *
import ursina
from system import color as c
#This appcation(game)'s FPS is low when use .exe,but running source code's FPS is high!
#Maybe it's good?Or bad???
#-----BUG-----#
#https://github.com/pyinstaller/pyinstaller/issues/8442
def start():
    #Window conf
    window.borderless = False
    window.title = "Blockgame - CMD Game"
    window.icon = "_internal/image/blockgame.ico"
    Text.default_font = '_internal/font/gamefont.ttf'
    from ursina.prefabs.first_person_controller import FirstPersonController
    app = Ursina(icon='_internal/image/blockgame.ico',title='Blockgame - CMD Game')
    #Audio
    distroy = Audio("_internal/audio/distroy.mp3", loop=False, autoplay=False)
    build = Audio("_internal/audio/build.mp3" , loop=False, autoplay=False)

#Voxel section
    class Voxel(Button):
        def __init__(self, position=(0, 0, 0)):
            super().__init__(
                parent=scene,
                position=position,
                model='cube',
                origin_y=.5,
                texture='_internal/image/cube.png',
                color=color.color(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )

#Input section
        def input(self, key):
            if self.hovered:
                if key == 'right mouse down':
                    voxel = Voxel(position=self.position + mouse.normal)
                    build.play()
                    print(c.blue+'[BLOCK]Build one block!'+c.end)

                if key == 'left mouse down':
                    destroy(self)
                    distroy.play()
                    print(c.blue+'[BLOCK]Distroy one block!'+c.end)

                if key == 'escape' or key == 'escape up':
                    application.quit()

                if key == 'f':
                    if mouse.locked == True:
                        mouse.locked = False
                    elif mouse.locked == False:
                        mouse.locked = True

#Generate section
    for z in range(8):
        for x in range(8):
            for y in range(-8, 0):
                voxel = Voxel(position=(x, y, z))

#Run section
    player = FirstPersonController()
    app.run()
