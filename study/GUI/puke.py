"""tkinter扑克牌"""

from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(relwidth=1, relheight=1)

        self.create_widget()

    def create_widget(self):
        self.photos = [PhotoImage(file="images/puke/puke"+str(i+1)+".gif") for i in range(10)]
        self.pukes = [Label(self.master, image=self.photos[i]) for i in range(10)]

        for i in range(10):
            self.pukes[i].place(x=20+i*60, y=50)

        self.pukes[0].bind_class("Label", "<Button-1>", self.xuanpai)
        # self.pukes[0].bind_class("Label", "<Enter> ", self.xuanpai)

    def xuanpai(self, e):
        print(e.widget.winfo_y())
        if e.widget.winfo_y() == 50:
            e.widget.place(y=30)
        else:
            e.widget.place(y=50)


if __name__ == '__main__':
    root = Tk()
    root.geometry("820x430+500+200")
    root.title("扑克")

    app = Application(root)
    app.pack()

    root.mainloop()