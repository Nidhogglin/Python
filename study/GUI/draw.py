# coding: utf-8
"""画图项目"""

from tkinter import *
from tkinter.colorchooser import *


class Application(Frame):
    """画图项目"""

    def __init__(self, master=None):
        super().__init__(master=master)     # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.bgcolor = "#000000"
        self.fgcolor = "#FF0000"
        self.lastDraw = 0
        self.startDrawFlag = False
        self.x = 0
        self.y = 0
        self.r = 0
        self.g = 0
        self.b = 0

        self.create_widget()

    def create_widget(self):
        """创建组件"""
        self.drawpad = Canvas(self.master, bg=self.bgcolor, width=win_width, height=win_height*0.9)
        self.drawpad.pack()

        btn_names = {"画笔": "pen", "直线": "line", "箭头直线": "lineArrow", "矩形": "rect", "橡皮擦": "eraser", "颜色": "color",
                     "清屏": "clear"}

        for btn, name in btn_names.items():
            Button(self.master, text=btn, name=name).pack(side=LEFT, padx=10)

        # 事件管理
        self.master.bind_class("Button", "<1>", self.eventMgr)
        self.drawpad.bind("<ButtonRelease-1>", self.stopDraw)

    def eventMgr(self, event):
        name = event.widget.winfo_name()
        print(name)
        if name == "line":
            self.drawpad.bind("<B1-Motion>", self.myline)
        elif name == "lineArrow":
            self.drawpad.bind("<B1-Motion>", self.mylineArrow)
        elif name == "rect":
            self.drawpad.bind("<B1-Motion>", self.myRect)
        elif name == "eraser":
            self.drawpad.bind("<B1-Motion>", self.myEraser)
        elif name == "color":
            self.change_color()
        elif name == "clear":
            self.drawpad.delete("all")
        elif name == "pen":
            self.drawpad.bind("<B1-Motion>", self.myPen)

    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0

    def startDraw(self, event):
        self.drawpad.delete(self.lastDraw)

        self.r += 1
        self.g += 2
        self.b += 3

        self.fgcolor = "#%02x%02x%02x" % (self.r % 255, self.g % 255, self.b % 255)

        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def myline(self, event):
        self.startDraw(event)

        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)

    def mylineArrow(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor, arrow=LAST)

    def myRect(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

    def myEraser(self, event):
        self.startDraw(event)
        self.drawpad.create_oval(event.x-10, event.y-10, event.x+10, event.y+10, fill=self.bgcolor)

    def change_color(self):
        c1 = askcolor(color=self.fgcolor, title="选择前景色")
        self.fgcolor = c1[1]
        self.r = int(self.fgcolor[1:3], base=16)
        self.g = int(self.fgcolor[3:5], base=16)
        self.b = int(self.fgcolor[5:7], base=16)

    def myPen(self, event):
        self.startDraw(event)
        self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
        self.x = event.x
        self.y = event.y

if __name__ == '__main__':
    root = Tk()
    win_width = 1000
    win_height = 600
    root.geometry("1000x600+500+200")
    root.title("画图")

    app = Application(root)
    app.pack()

    root.mainloop()
