import sys
total = 0
progress = 0
bar_length = 40

def setbar(total_count):
    global total
    total = total_count

def bar():
    global total, progress
    if total == 0:
        print("Error:setbar()")
        return

    progress += 1
    percent = progress / total
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rLoading: [{0}] {1}/{2}".format(arrow + spaces, progress, total))
    sys.stdout.flush()