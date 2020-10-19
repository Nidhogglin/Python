#!usr/bin/env python3
# coding: utf-8
# @time :2020/10/19 17:09

from tkinter import *
import tkinter.messagebox as tm
import PythonMagick


class Application(Tk):

    def __init__(self, master=None):
        Tk.__init__(self, master)
        Button(text='hello', command=self.button_event).pack(anchor='nw')

    def button_event(self):
        self.tm = tm.showinfo(title='信息', message='这是信息')


a = Application()
a.geometry('500x300')
a.title('我的窗口')
a.mainloop()