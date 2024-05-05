#New calender
def start():
    import tkinter as tk


    class Calc(tk.Tk):
        """计算器窗体类"""
        def __init__(self):
            """初始化实例"""
            tk.Tk.__init__(self)
            self.title("New Calender")
            self.memory = 0  # 暂存数值
            self.create()

        def create(self):
            """创建界面"""
            btn_list = ["C", "M->", "->M", "/",
                        "7", "8", "9", "*",
                        "4", "5", "6", "-",
                        "1", "2", "3", "+",
                        "+/-", "0", ".", "="]
            r = 1
            c = 0
            for b in btn_list:
                self.button = tk.Button(self, text=b, width=5,
                                        command=(lambda x=b: self.click(x)))
                self.button.grid(row=r, column=c, padx=3, pady=6)
                c += 1
                if c > 3:
                    c = 0
                    r += 1
            self.entry = tk.Entry(self, width=24, borderwidth=2,
                                  bg="yellow", font=("Consolas", 12))
            self.entry.grid(row=0, column=0, columnspan=4, padx=8, pady=6)

        def click(self, key):
            """响应按钮"""
            if key == "=":  # 输出结果
                result = eval(self.entry.get())
                self.entry.insert(tk.END, " = " + str(result))
            elif key == "C":  # 清空输入框
                self.entry.delete(0, tk.END)
            elif key == "->M":  # 存入数值
                self.memory = self.entry.get()
                if "=" in self.memory:
                    ix = self.memory.find("=")
                    self.memory = self.memory[ix + 2:]
                self.title("M=" + self.memory)
            elif key == "M->":  # 取出数值
                if self.memory:
                    self.entry.insert(tk.END, self.memory)
            elif key == "+/-":  # 正负翻转
                if "=" in self.entry.get():
                    self.entry.delete(0, tk.END)
                elif self.entry.get()[0] == "-":
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, "-")
            else:  # 其他键
                if "=" in self.entry.get():
                    self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, key)

    Calc().mainloop()