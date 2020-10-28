#!usr/bin/env python3
# coding: utf-8
# @time :2020/10/16 13:42

import tkinter as tk

# 创建窗口实例
win = tk.Tk()
# 设置窗口标题
win.title('My window')
# 设置窗口尺寸
win.geometry('500x500')


def demo():

    def button_event():
        var1 = e1.get()
        var2 = e2.get()
        text.insert('insert', var1)
        text.insert('end', var2)

    def button2_event():
        value = lb.get(lb.curselection())
        var_l.set(value)

    # 创建标签
    label = tk.Label(win, text='你好啊，小老弟！', bg='blue', font=('Arial', 12), width=30, height=2)
    # 放置标签，不放置不会显示在窗口上
    label.pack()
    # 创建按钮并放置
    button = tk.Button(win, text='按钮', bg='red', font=('Arial', 12), width=10, height=1, command=button_event)
    button.pack()
    # 创建文本输入框并放置
    e1 = tk.Entry(win, show=None, font=('Arial', 14))
    e2 = tk.Entry(win, show='*', font=('Arial', 14))
    e1.pack()
    e2.pack()
    # 创建Text文本框并放置
    text = tk.Text(win, height=3)
    text.pack()
    # 创建Listbox并放置
    var_l = tk.StringVar()  # 创建变量，用var_l用来接收鼠标点击具体选项的内容
    label2 = tk.Label(win, bg='green', fg='yellow', width=20, font=('Arial', 12), textvariable=var_l)
    label2.pack()
    button2 = tk.Button(win, text="显示选择项", width=15, height=2, command=button2_event)
    button2.pack()
    var_lb = tk.StringVar()  # 创建Listbox并为其添加内容
    var_lb.set((1, 2, 3, 4))
    lb = tk.Listbox(win, listvariable=var_lb)
    list_items = [11, 22, 33, 44]
    for item in list_items:
        lb.insert('end', item)  # 从最后一个位置开始加入值
    lb.insert(1, 'first')   # 在第2个位置加入'first'字符
    lb.insert(2, 'second')  # 在第3个位置加入'second'字符
    lb.delete(0)            # 删除第1个位置的字符
    lb.pack()


# 单选框
def radio_button():
    var = tk.StringVar()   # 定义一个var用来将radiobutton的值和Label的值联系在一起
    label = tk.Label(win, bg='yellow', width=20, text='empty')
    label.pack()

    def print_selection():
        label.config(text='你选择了：' + var.get())

    rb1 = tk.Radiobutton(win, text='选项A', variable=var, value='A', command=print_selection)
    rb2 = tk.Radiobutton(win, text='选项B', variable=var, value='B', command=print_selection)
    rb3 = tk.Radiobutton(win, text='选项C', variable=var, value='C', command=print_selection)
    rb1.pack()
    rb2.pack()
    rb3.pack()


# 复选框
def check_button():
    label = tk.Label(win, width=20, text='empty')
    label.pack()

    def print_selection():
        if (var1.get() == 1) & (var2.get() == 0):
            label.config(text='人生苦短，我用Python', bg='yellow')
        elif (var1.get() == 0) & (var2.get() == 1):
            label.config(text='人生苦短， Let‘s Go', bg='blue')
        elif (var1.get() == 0) & (var2.get() == 0):
            label.config(text="打扰了", bg='white')
        else:
            label.config(text='为什么要做选择，我都要', bg='red')

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    cb1 = tk.Checkbutton(win, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
    cb1.pack()
    cb2 = tk.Checkbutton(win, text='Golang', variable=var2, onvalue=1, offvalue=0, command=print_selection)
    cb2.pack()


def scale():
    label = tk.Label(win, bg='green', fg='white', width=20, text='empty')
    label.pack()
    var = tk.DoubleVar()

    def print_selection(var):
        label.config(text='滚动条位置：' + var)

    s = tk.Scale(win, label='滚动条', from_=0, to=10, orient=tk.HORIZONTAL, length=200, variable=var,
                 showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
    s.pack()


# 图片文件必须为全局变量才能显示
image_file = tk.PhotoImage(file='GUI_test.gif')


# 画布
def canvas():
    can = tk.Canvas(win, bg='green', height=200, width=500)

    # 图片文件必须为全局变量才能显示
    global image_file
    image = can.create_image(250, 0, image=image_file, anchor='n')  # 图片锚定点（n:图片顶端的中间点位置）放在画布（250,0）坐标处
    rect = can.create_rectangle(20, 20, 110, 110, fill='red')  # 画矩形
    can.create_oval(220, 150, 270, 200, fill='blue')  # 画圆
    can.create_arc(150, 100, 200, 150, start=0, extent=180)  # 画扇形 从0度打开收到180度结束
    can.pack()

    def move():
        can.move(rect, 2, 2)
        can.move(image, 0, 2)

    tk.Button(win, text='移动图形', command=move).pack()


# 菜单条
def menu():
    label = tk.Label(win, text='', width=20, height=2)
    label.pack()

    count = 0

    def command():
        nonlocal count
        count += 1
        label.config(text='第'+str(count)+'次点击')

    # 创建主菜单
    menu_bar = tk.Menu(win)

    # 创建一级菜单：菜单
    file_menu = tk.Menu(menu_bar, tearoff=0)  # 默认不下拉
    menu_bar.add_cascade(label='菜单', menu=file_menu)
    file_menu.add_command(label='新建', command=command)
    file_menu.add_command(label='打开', command=command)
    file_menu.add_command(label='保存', command=command)
    file_menu.add_command(label='另存为', command=command)
    file_menu.add_separator()
    file_menu.add_command(label='退出', command=win.quit)

    # 创建一级菜单：编辑
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='编辑', menu=edit_menu)
    edit_menu.add_command(label='剪切', command=command)
    edit_menu.add_command(label='粘贴', command=command)
    edit_menu.add_command(label='复制', command=command)

    # 创建二级菜单
    sub_menu = tk.Menu(file_menu)
    file_menu.add_cascade(label='其他', menu=sub_menu, underline=0)
    sub_menu.add_command(label='导入', command=command)

    win.config(menu=menu_bar)


# 框架
def frame_demo():
    tk.Label(win, text='在窗口win', bg='red', font=('Arial', 16)).pack()  # 可以创建时直接放置

    # 创建一个主frame， 放在主win窗口上
    frame = tk.Frame(win)
    frame.pack()

    # 创建二级框架， 放在主frame上
    frame_l = tk.Frame(frame)
    frame_l.pack(side='left')
    frame_r = tk.Frame(frame)
    frame_r.pack(side='right')

    # 在二级框架上创建标签
    tk.Label(frame_l, text='在左二级框架上1', bg='green').pack()
    tk.Label(frame_l, text='在左二级框架上2', bg='green').pack()
    tk.Label(frame_l, text='在左二级框架上3', bg='green').pack()
    tk.Label(frame_r, text='在右二级框架上1', bg='yellow').pack()
    tk.Label(frame_r, text='在右二级框架上2', bg='yellow').pack()


def message_box():
    import tkinter.messagebox as tm

    def info():
        tm.showinfo(title='信息', message='这是信息')

    def warning():
        tm.showwarning(title='警告', message='这是警告')

    def error():
        tm.showerror(title='错误', message='这是错误')

    def ask_question():
        result = tm.askquestion(title='问题', message='这是问题')
        print(result)

    def ask_yesno():
        print(tm.askyesno(title='是否', message='这是是否'))

    def ask_okcancel():
        print(tm.askokcancel(title='确定取消', message='这是确定取消'))

    tk.Button(win, text='信息对话框', bg='green', font=('Arial', 14), command=info).pack()
    tk.Button(win, text='警告对话框', bg='yellow', font=('Arial', 14), command=warning).pack()
    tk.Button(win, text='错误对话框', bg='red', font=('Arial', 14), command=error).pack()
    tk.Button(win, text='问题对话框', bg='green', font=('Arial', 14), command=ask_question).pack()
    tk.Button(win, text='是否对话框', bg='yellow', font=('Arial', 14), command=ask_yesno).pack()
    tk.Button(win, text='确定取消对话框', bg='red', font=('Arial', 14), command=ask_okcancel).pack()


# 放置方法：Grid
def grid():
    for i in range(3):
        for j in range(3):
            tk.Label(win, text=123456).grid(row=i, column=j, pady=10, padx=10, ipadx=10, ipady=10)


# 放置方法：Pack
def pack():
    tk.Label(win, text='P', fg='red').pack(side='top')  # 上
    tk.Label(win, text='P', fg='red').pack(side='bottom')  # 下
    tk.Label(win, text='P', fg='red').pack(side='left')  # 左
    tk.Label(win, text='P', fg='red').pack(side='right')  # 右
    tk.Button(win, text='A', fg='red').pack(anchor='ne', fill='y', expand='yes')


# 放置方法：Place
def place():
    # 后面的参数 anchor='nw'，就是锚定点是西北角
    tk.Label(win, text='place', font=('Arial', 20), width=20, height=3, bg='red').place(x=50, y=100, anchor='nw')


if __name__ == '__main__':
    demo()
    # radio_button()
    # check_button()
    # scale()
    # canvas()
    # menu()
    # frame_demo()
    # message_box()
    # grid()
    # pack()
    # place()

    # 主窗口循环显示
    win.mainloop()

