"""经典的GUI程序写法"""

from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import *


class Application(Frame):
    """一个经典的GUI程序的写法"""

    def __init__(self, master=None):
        super().__init__(master=master)     # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()

        self.create_widget()

    def create_widget(self):
        """创建组件"""
        Button(text="选择背景色", command=self.test).pack()

    def test(self):
        c = askcolor(color='red', title="选择背景色")
        print(c)
        self.master.config(bg=c[1])


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300+500+200")
    root.title("经典GUI程序")

    app = Application(root)
    app.pack()

    root.mainloop()
