# -*- coding: utf-8 -*-
"""
Codex appcation
"""
from tkinter.filedialog import *
def start():
    import  tkinter  as  tk   #导入Tkinter
    import  tkinter.ttk  as  ttk   #导入Tkinter.ttk
    from  tkinter.scrolledtext  import ScrolledText  #导入ScrolledText


    mytitle='Python Codex'

    #建立主窗口
    root=tk.Tk()
    root.title(mytitle)
    root.geometry('{}x{}+{}+{}'.format(800, 600, 100, 100))

    #放几个按钮
    frame=tk.Frame(root)
    button1=tk.Button(frame,text='New File')
    button2=tk.Button(frame,text='Load File')
    button3=tk.Button(frame,text='Save File')
    button1.pack(side=tk.LEFT)
    button2.pack(side=tk.LEFT)
    button3.pack(side=tk.LEFT)
    frame.pack(side=tk.TOP,fill=tk.BOTH)

    #放置一个文本框
    textPad= ScrolledText(bg='white', height=10)
    textPad.pack(fill=tk.BOTH, expand=1)
    textPad.focus_set()

    #实现按钮功能
    def btnfunc01():  #新文件
        textPad.delete(1.0,tk.END)

    def btnfunc02(): #读取文件
        filename = askopenfilename(defaultextension='.py')
        if filename != '':
            textPad.delete(1.0,tk.END)#delete all
            f = open(filename,'r',encoding='utf-8',errors='ignore')
            textPad.insert(1.0,f.read())
            f.close()


    def btnfunc03(): #另存文件
        filename = asksaveasfilename(initialfile = 'newfile',defaultextension ='.py')
        if filename != '':
            fh = open(filename,'w',encoding='utf-8',errors='ignore')
            msg = textPad.get(1.0,tk.END)
            fh.write(msg)
            fh.close()

    #为按钮设置功能
    button1['command']=lambda:btnfunc01()
    button2['command']=lambda:btnfunc02()
    button3['command']=lambda:btnfunc03()

    root.mainloop()  	#进入Tkinter消息循环

