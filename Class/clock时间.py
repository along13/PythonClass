import tkinter as tk
from time import strftime
from tkinter import messagebox


class ClockApp:
    def __init__(self, root):
        try:
            self.root = root
            self.root.title("数字时钟")

            # 设置窗口大小和位置
            self.root.geometry("400x200")
            self.root.configure(bg='black')

            # 防止窗口大小改变
            self.root.resizable(False, False)

            # 创建时间标签
            self.time_label = tk.Label(
                self.root,
                font=('Arial', 60, 'bold'),
                background='black',
                foreground='#00ff00'
            )
            self.time_label.pack(anchor='center', pady=50)

            # 创建日期标签
            self.date_label = tk.Label(
                self.root,
                font=('Arial', 20),
                background='black',
                foreground='#00ff00'
            )
            self.date_label.pack(anchor='center')

            # 更新时间
            self.update_time()

        except Exception as e:
            messagebox.showerror("错误", f"初始化时钟时出错: {str(e)}")
            self.root.destroy()

    def update_time(self):
        try:
            # 获取并显示当前时间和日期
            current_time = strftime('%H:%M:%S')
            current_date = strftime('%Y-%m-%d')
            self.time_label.config(text=current_time)
            self.date_label.config(text=current_date)
            # 每1000毫秒（1秒）更新一次
            self.root.after(1000, self.update_time)

        except Exception as e:
            messagebox.showerror("错误", f"更新时间时出错: {str(e)}")


def main():
    try:
        root = tk.Tk()
        app = ClockApp(root)
        root.mainloop()
    except Exception as e:
        print(f"程序启动错误: {str(e)}")


if __name__ == "__main__":
    main()