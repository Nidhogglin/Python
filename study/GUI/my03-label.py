"""tkinter中Label使用"""

from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(relwidth=1, relheight=1)

        self.create_widget()

    def create_widget(self):
        # 显示图片
        global photo
        photo = PhotoImage(file="images/welcome.gif")
        self.label01 = Label(self, image=photo)
        self.label01.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300+500+200")
    root.title("Label测试")

    app = Application(root)
    app.pack()

    root.mainloop()
