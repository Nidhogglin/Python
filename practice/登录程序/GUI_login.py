#!usr/bin/env python3
# coding: utf-8
# @time :2020/10/19 15:58

import tkinter as tk
import os

win = tk.Tk()

# 设置窗口尺寸
win_width = 500
win_height = 300

# 获取屏幕分辨率
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x = int((screen_width-win_width)/2)
y = int((screen_height-win_height)/2)

# 设置主窗口标题
win.title('登录')
# 设置窗口出生违章在屏幕居中
win.geometry('%sx%s+%s+%s' % (win_width, win_height, x, y))
# 设置窗口图标
win.iconbitmap('./image/title1.ico')


win.mainloop()