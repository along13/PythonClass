from tkinter import *
def show1(event):# <Button-1>
    lb.configure(text='哦，左键')

def show3(event):# <Button-3>
    lb.configure(text='哦，右键')

root = Tk()
root.title('响应事件')
root.geometry('300x200')

lb = Label(root, text='', bg='white')
lb.pack()

btn = Button(root, text='点我')# <Button>
btn.bind('<Button-1>', show1)
btn.bind('<Button-3>', show3)
btn.focus_set()
btn.pack()
root.mainloop()