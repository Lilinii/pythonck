import tkinter as tk
from tkinter import messagebox

import login as login

root = tk.Tk()
root.geometry('300x180')
root.title('学生宿舍管理登录页')
# 获取输入信息
username = tk.StringVar()
password = tk.StringVar()

# 创建页面
page = tk.Frame(root)
page.pack()

tk.Label(page).grid(row=0, column=0)

tk.Label(page, text='学号: ').grid(row=1, column=1)
tk.Entry(page, textvariable=username).grid(row=1, column=2)

tk.Label(page, text='密码: ').grid(row=2, column=1, pady=10)  # 行，列，上下间隔
tk.Entry(page, textvariable=password).grid(row=2, column=2)


def login():
    name = username.get()
    pwd = password.get()
    print(name, pwd)
    # 判断模型
    if name == '2218300123' and pwd == '2004':
        print('登陆成功')
    else:
        messagebox.showwarning(title='警告', message='登录失败请检查账号密码是否正确！')


tk.Button(page, text='登录', command=login).grid(row=3, column=1, pady=10)
tk.Button(page, text='退出', command=page.quit).grid(row=3, column=2)
root.mainloop()




