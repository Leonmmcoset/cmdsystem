#Test appcation
import turtle as t
def start():
    a = int(input('Section:'))
    if a == 1:
        for i in range(4):
            t.forward(50)
            t.right(90)
    if a == 2:
        for i in range(3):
            t.forward(50)
            t.right(120)
    if a == 3:
        for i in range(8):
            t.forward(50)
            t.right(45)
#Test
# import sys
# sys.stderr.write('Test')
