"""GUI简易笔记本练习"""

from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *


class Application(Frame):
    """一个经典的GUI程序的写法"""

    def __init__(self, master=None):
        super().__init__(master=master)     # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.place(relwidth=1, relheight=1)

        self.create_widget()

    def create_widget(self):

        self.fileName = None

        # 创建问题输入框
        self.textPad = Text(self.master, font=("新宋体", 12))
        self.textPad.place(relwidth=1, relheight=1)

        # 创建菜单栏
        self.menuBar = Menu(self.master)

        self.fileMenu = Menu(self.menuBar)
        self.editMenu = Menu(self.menuBar)
        self.helpMenu = Menu(self.menuBar)

        # 放置菜单栏
        self.menuBar.add_cascade(label="文件(F)", menu=self.fileMenu)
        self.menuBar.add_cascade(label="编辑(E)", menu=self.editMenu)
        self.menuBar.add_cascade(label="帮助(H)", menu=self.helpMenu)

        # 添加功能
        self.fileMenu.add_command(label="新建 Ctrl+N", command=self.new_file)
        self.fileMenu.add_command(label="打开 Ctrl+O", command=self.open_file)
        self.fileMenu.add_command(label="保存 Ctrl+S", command=self.save_file)
        self.fileMenu.add_command(label="另存为 Ctrl+A", command=self.new_file)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="退出 Ctrl+Q", command=self.master.quit)

        # 放置主菜单
        self.master.config(menu=self.menuBar)

        # 上下文菜单
        self.contextMenu = Menu(self.master)
        self.contextMenu.add_command(label="背景颜色", command=self.bg_color)
        self.master.bind("<Button-3>", self.create_context_menu)

        # 绑定快捷键
        self.master.bind("<Control-n>", lambda event: self.new_file())
        self.master.bind("<Control-o>", lambda event: self.open_file())
        self.master.bind("<Control-s>", lambda event: self.save_file())
        # self.master.bind("<Control-a>", lambda event: self.saveas_file())
        self.master.bind("<Control-q>", lambda event: self.master.quit())


    def new_file(self):
        self.textPad.delete("1.0", "end")
        self.fileName = None

    def open_file(self):
        self.textPad.delete("1.0", "end")
        with askopenfile(title="选择文本文档", filetypes=[("文本文档", "*.txt")]) as f:
            self.fileName = f.name
            print(f.name)
            self.textPad.insert(INSERT, f.read())

    def save_file(self):
        if not self.fileName:
            self.fileName = asksaveasfilename(title="保存", initialfile="未命名.txt", filetypes=[("文本文档", "*.txt")],
                                              defaultextension=".txt")
        if self.fileName:
            with open(self.fileName, "w", encoding="utf-8") as f:
                f.write(self.textPad.get("1.0", "end"))

    def create_context_menu(self, event):
        self.contextMenu.post(event.x_root, event.y_root)

    def bg_color(self):
        c1 = askcolor(color='green', title="选择背景颜色")
        self.textPad.config(bg=c1[1])


if __name__ == '__main__':
    root = Tk()
    root.geometry("1000x600+500+200")
    root.title("简易记事本")

    app = Application(root)
    app.pack()

    root.mainloop()
