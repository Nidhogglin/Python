"""tkinter事件绑定测试"""

from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(relwidth=1, relheight=1)

        self.create_widget()

    def create_widget(self):
        self.btn01 = Button(self, text="btn01", command=self.bind_test1)
        self.btn01.pack(side=LEFT)

        self.btn02 = Button(self, text="btn02")
        self.btn02.pack(side=LEFT)
        self.btn02.bind("<Button-1>", self.bind_test2)

        self.btn02.bind_class("Button", "<Button-3>", self.bind_test3)


    def bind_test1(self):
        print("普通的绑定事件，不能获取控件信息")

    def bind_test2(self, event):
        print("bind绑定事件，需要传入event")
        print(event.widget.winfo_geometry())

    def bind_test3(self, event):
        print("bind_class绑定事件，给一类组件绑定事件")
        print(event.widget)



if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300+500+200")
    root.title("Label测试")

    app = Application(root)
    app.pack()

    root.mainloop()
