from tkinter import *
def Mysel():
    choice = var.get()
    choice_dict = {0:'甲', 1:'乙', 2:'丙'}
    s = "你选择了{}".format(choice_dict[choice])
    lb.configure(text=s)

root = Tk()
root.title("单选按钮")
root.geometry("300x200")
lb = Label(root, text="nn")
lb.pack()

var = IntVar()

rd1 = Radiobutton(root, text="甲", variable=var, value=0, command=Mysel)
rd1.pack()

rd2 = Radiobutton(root, text="乙", variable=var, value=1, command=Mysel)
rd2.pack()

rd3 = Radiobutton(root, text="丙", variable=var, value=2, command=Mysel)
rd3.pack()

root.mainloop()