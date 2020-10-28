#!usr/bin/env python3
# coding: utf-8
# @time :2020/10/19 17:09

import winreg
from tkinter import *
import tkinter.messagebox as tm
import tkinter.filedialog
import tkinter.scrolledtext as ts
import os
import subprocess
import win32gui
from cmd import Cmd


def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]


desktop_path = get_desktop()

win = Tk()
win.geometry('950x500')
win.title('我的窗口')


def screen_clear():
    scr.delete('1.0', 'end')


Button(text='清屏', command=screen_clear).pack(side='bottom')


scr = ts.ScrolledText(win, width=60, bg='#55C85A', font=(None, 12), relief='solid',)
scr.pack(side='left', fill=Y, padx=5, pady=5)

cmd = 'adb shell getprop | findstr vin'
scr.insert('insert', cmd+'\n', )
f = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in f.stdout.readlines():
    scr.insert('insert', line.decode())



def b_event():
    print(scr.get('end-2l', 'end')+'1')
    scr.tag_config('a', foreground="blue", underline=1)
    # scr.insert('end', ('a', ))
    # scr.delete('1.0', 'end')


Button(text='点击', command=b_event).pack()



win.mainloop()
