from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI程序")
root.geometry("500x300+300+150")

btn01 = Button(root)
btn01["text"] = "点我有惊喜"
btn01.pack()


def surprise(e):
    messagebox.showinfo("surprise", "哒哒")


btn01.bind("<Button>", surprise)


def scare():
    messagebox.showerror("scare", "哒哒哒")


btn02 = Button(root, text="点我有惊吓", command=scare)
btn02.pack()

root.mainloop()