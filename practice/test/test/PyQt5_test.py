#!usr/bin/env python3
# coding: utf-8
# @time :2020/10/26 17:56

import win32gui
import pygetwindow as gw
from tkinter import *
I

root = Tk()
root.geometry('800x500')
hwnd = win32gui.FindWindow(None, u"管理员: C:\\windows\\system32\\cmd.exe")
win32gui.SetParent(hwnd, int(root.winfo_id()))

frame1 = Frame(root, width=400, height=50)


titles = gw.getAllTitles()
print(titles)

root.mainloop()