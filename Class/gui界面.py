import tkinter as tk

root = tk.Tk()#创建窗口
root.title('Hello')#窗口标题
root.geometry("300x200")#窗口大小
root.maxsize(500, 500)  # 窗口的最大尺寸
root.minsize(200, 200)  # 窗口的最小尺寸
# root.resizable(False, False)#窗口是否可变
# root.state('zoomed')
root.iconbitmap("question")
root.configure(bg='#CD5C5C')  # 窗口的背景颜色
lb = tk.Label(root,text='Hello World')#创建标签
lb.pack()#将标签添加到窗口
root.mainloop()#运行窗口
