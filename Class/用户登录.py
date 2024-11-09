import tkinter as tk
from tkinter import messagebox


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("用户登录")
        self.root.geometry("300x200")
        self.root.configure(bg='#f0f0f0')
        self.root.resizable(False, False)

        # 模拟用户数据库
        self.users = {
        "admin": "123456",
        "user1": "password123",
        "test": "test123"
        }

        # 创建主框架
        self.frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20)#背景色,padx pady边距
        self.frame.pack(expand=True)

        # 用户名
        self.username_label = tk.Label(
            self.frame,
            text="用户名:",
            bg='#f0f0f0',
            font=('Arial', 12)
        )
        self.username_label.grid(row=0, column=0, sticky='e', pady=5)

        self.username_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.username_entry.grid(row=0, column=1, pady=5)

        # 密码
        self.password_label = tk.Label(
            self.frame,
            text="密码:",
            bg='#f0f0f0',
            font=('Arial', 12)
        )
        self.password_label.grid(row=1, column=0, sticky='e', pady=5)

        self.password_entry = tk.Entry(
            self.frame,
            show="*",
            font=('Arial', 12)
        )
        self.password_entry.grid(row=1, column=1, pady=5)

        # 登录按钮
        self.login_button = tk.Button(
            self.frame,
            text="登录",
            command=self.login,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 12),
            width=10
        )
        self.login_button.grid(row=2, column=0, columnspan=2, pady=15)

        # 结果标签
        self.result_label = tk.Label(
            self.frame,
            text="",
            bg='#f0f0f0',
            font=('Arial', 12)
        )
        self.result_label.grid(row=3, column=0, columnspan=2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users:
            if self.users[username] == password:
                self.result_label.config(
                    text="登录成功！",
                    fg="green",
                )
            else:
                self.result_label.config(
                    text="密码错误！",
                    fg="red"
                )
        else:
            self.result_label.config(
                text="用户名不存在！",
                fg="red"
            )


def main():
    try:
        root = tk.Tk()
        app = LoginApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("错误", f"程序启动错误: {str(e)}")


if __name__ == "__main__":
    main()