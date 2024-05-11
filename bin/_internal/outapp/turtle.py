#Test appcation
from turtle import *
def start():
    a = int(input('Section:'))
    if a == 1:
        for i in range(4):
            forward(50)
            right(90)
    if a == 2:
        for i in range(3):
            forward(50)
            right(120)
    if a == 3:
        for i in range(8):
            forward(50)
            right(45)
#Test
import sys
sys.stderr.write('Test')
