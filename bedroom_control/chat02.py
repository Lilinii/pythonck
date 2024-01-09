import tkinter as tk
from tkinter import messagebox

# 管理员类
class Administrator:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# 管理员列表
administrators = []
# 管理员登录界面
def open_admin_login():
    admin_login_window = tk.Toplevel(root)
    admin_login_window.title('管理员登录')

    tk.Label(admin_login_window, text='用户名:').grid(row=0, column=0)
    admin_username = tk.Entry(admin_login_window)
    admin_username.grid(row=0, column=1)

    tk.Label(admin_login_window, text='密码:').grid(row=1, column=0)
    admin_password = tk.Entry(admin_login_window, show='*')
    admin_password.grid(row=1, column=1)

    def admin_login():
        username = admin_username.get()
        pwd = admin_password.get()
        for admin in administrators:
            if admin.username == username and admin.password == pwd:
                open_admin_dashboard()
                admin_login_window.destroy()
                return
        messagebox.showerror('错误', '用户名或密码错误')

    tk.Button(admin_login_window, text='登录', command=admin_login).grid(row=2, column=0, columnspan=2)

# 管理员注册界面
def open_admin_register():
    admin_register_window = tk.Toplevel(root)
    admin_register_window.title('管理员注册')

    tk.Label(admin_register_window, text='用户名:').grid(row=0, column=0)
    new_admin_username = tk.Entry(admin_register_window)
    new_admin_username.grid(row=0, column=1)

    tk.Label(admin_register_window, text='密码:').grid(row=1, column=0)
    new_admin_password = tk.Entry(admin_register_window, show='*')
    new_admin_password.grid(row=1, column=1)

    def admin_register():
        username = new_admin_username.get()
        pwd = new_admin_password.get()
        for admin in administrators:
            if admin.username == username:
                messagebox.showerror('错误', '用户名已存在')
                return
        new_admin = Administrator(username, pwd)
        administrators.append(new_admin)
        messagebox.showinfo('成功', '注册成功')
        admin_register_window.destroy()

    tk.Button(admin_register_window, text='注册', command=admin_register).grid(row=2, column=0, columnspan=2)

# 管理员面板
def open_admin_dashboard():
    admin_dashboard_window = tk.Toplevel(root)
    admin_dashboard_window.title('管理员面板')

    # 在这里添加管理员面板的功能，例如管理学生信息和维修请求等

root = tk.Tk()
root.title("主页面")

tk.Button(root, text="管理员登录", command=open_admin_login).pack()
tk.Button(root, text="管理员注册", command=open_admin_register).pack()

# 在这里可以添加其他功能，比如学生登录等

root.mainloop()
