#System conf:time system.
def time():
    import time as t
    import sys as s
    s.setrecursionlimit(3000)
    global ctime_
    global time_
    ctime_ = t.ctime()
    time_ = t.time()
    print('Time:',ctime_)
    print('Timestamp:',time_)