"""经典的GUI程序写法"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序的写法"""

    def __init__(self, master=None):
        super().__init__(master=master)     # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()

        self.create_widget()

    def create_widget(self):
        """创建组件"""
        self.btn01 = Button(self)
        self.btn01["text"] = "点我有惊喜"
        self.btn01["command"] = self.surprise
        self.btn01.pack()

        self.btnQuit = Button(self, text="退出", command=self.master.destroy)
        self.btnQuit.pack()

    def surprise(self):
        messagebox.showinfo("惊喜", "哒哒！")


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300+500+200")
    root.title("经典GUI程序")

    app = Application(root)
    app.pack()

    root.mainloop()
