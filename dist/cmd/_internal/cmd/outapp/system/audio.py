from pygame import *    #I wish I can say:import pygame as pg (Ofcourse not import pygame as pygame :(  ).
def playaudio(music_path):
    mixer.init()
    mixer.music.load(music_path)
    mixer.music.play()