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

        self.v = StringVar(self)
        self.v.set("LQQ")
        self.optionMenu = OptionMenu(self, self.v, "LZR", "LQQ", "LKL", "LFD")
        self.optionMenu.pack()
        Button(self, text="btn01", command=self.test).pack()

        self.scale = Scale(self, from_=10, to=50, length=200, tickinterval=5, orient=HORIZONTAL,
                           command=self.scale_slide)
        self.scale.pack()

        self.label = Label(self, text="Nidhogg Lin")
        self.label.pack()

    def scale_slide(self, value):
        print("滑块的值:", value)
        newFont = ("宋体", value)
        self.label.config(font=newFont)

    def test(self):
        print(self.v.get())


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300+500+200")
    root.title("经典GUI程序")

    app = Application(root)
    app.pack()

    root.mainloop()
