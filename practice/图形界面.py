#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/27 20:03

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # self.createWidgets()
        self.createWidgets2()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello,world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def createWidgets2(self):
        self.nameIput = Entry(self)
        self.nameIput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameIput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


if __name__ == '__main__':
    app = Application()
    app.master.title('Hell World')
    app.mainloop()
