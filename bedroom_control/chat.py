import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('300x250')
root.title('学生宿舍管理登录页')

# 存储学生信息的列表
students = []


class Student:
    def __init__(self, student_id, password):
        self.student_id = student_id
        self.password = password  # 注意：实际应用中应加密存储密码


# 添加学生信息的函数
def add_student(student_id, password):
    new_student = Student(student_id, password)
    students.append(new_student)


# 创建登录页面
login_page = tk.Frame(root)
login_page.pack()

tk.Label(login_page, text='学号: ').grid(row=1, column=1)
username = tk.StringVar()
tk.Entry(login_page, textvariable=username).grid(row=1, column=2)

tk.Label(login_page, text='密码: ').grid(row=2, column=1, pady=10)
password = tk.StringVar()
tk.Entry(login_page, textvariable=password).grid(row=2, column=2)


def login():
    student_id = username.get()
    pwd = password.get()
    for student in students:
        if student.student_id == student_id and student.password == pwd:
            messagebox.showinfo(title='登录信息', message='登录成功！')
            return
    messagebox.showwarning(title='警告', message='登录失败请检查账号密码是否正确！')


tk.Button(login_page, text='登录', command=login).grid(row=3, column=1, pady=10)
tk.Button(login_page, text='退出', command=root.quit).grid(row=3, column=2)


# 创建注册页面
def open_register_page():
    register_page = tk.Toplevel(root)
    register_page.geometry('300x180')
    register_page.title('注册新学生')

    tk.Label(register_page, text='学号: ').grid(row=1, column=1)
    new_username = tk.StringVar()
    tk.Entry(register_page, textvariable=new_username).grid(row=1, column=2)

    tk.Label(register_page, text='密码: ').grid(row=2, column=1, pady=10)
    new_password = tk.StringVar()
    tk.Entry(register_page, textvariable=new_password).grid(row=2, column=2)

    def register():
        add_student(new_username.get(), new_password.get())
        messagebox.showinfo(title='注册信息', message='注册成功！')
        register_page.destroy()

    tk.Button(register_page, text='注册', command=register).grid(row=3, column=1, pady=10)
    tk.Button(register_page, text='取消', command=register_page.destroy).grid(row=3, column=2)


tk.Button(login_page, text='注册', command=open_register_page).grid(row=4, column=1, pady=10)

root.mainloop()
