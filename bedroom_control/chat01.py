import tkinter as tk
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
root.geometry('300x250')
root.title('学生宿舍管理登录页')

# 学生，维修列表
students = []
repair_requests = []


# 管理员类
class Administrator:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# 管理员列表
administrators = []


# 学生类
class Student:
    def __init__(self, student_id, password):
        self.student_id = student_id
        self.password = password
        self.attendance = {}


# 维修信息类
class RepairRequest:
    def __init__(self, student_id, issue):
        self.student_id = student_id
        self.issue = issue
        self.status = 'Pending'


# 添加学生信息（注册）
def add_student(student_id, password):
    students.append(Student(student_id, password))


# 登录学生账号密码
def login():
    student_id = username.get()
    pwd = password.get()
    for student in students:
        if student.student_id == student_id and student.password == pwd:
            # 打开学生宿舍界面
            open_student_dashboard(student)
            return
    messagebox.showwarning(title='警告', message='登录失败请检查账号密码是否正确！')


# 学生宿舍面板
def open_student_dashboard(student):
    dashboard = tk.Toplevel(root)
    dashboard.title('学生面板')

    # 学生签到系统
    tk.Label(dashboard, text='学生签到系统').pack()
    attendance_list = tk.Listbox(dashboard)
    for date, status in student.attendance.items():
        attendance_list.insert(tk.END, f"{date}: {status}")
    attendance_list.pack()

    def sign_in():
        today = datetime.now().strftime("%Y-%m-%d")
        student.attendance[today] = '已签到'
        attendance_list.insert(tk.END, f"{today}: 已签到")

    tk.Button(dashboard, text='今日签到', command=sign_in).pack()

    # 公寓保修系统
    tk.Label(dashboard, text='公寓保修系统').pack()
    repair_text = tk.Text(dashboard, height=3)
    repair_text.pack()

    def submit_repair():
        issue = repair_text.get("1.0", tk.END).strip()
        if issue:
            repair_requests.append(RepairRequest(student.student_id, issue))
            messagebox.showinfo('提交成功', '您的维修请求已提交')
            repair_text.delete("1.0", tk.END)

    tk.Button(dashboard, text='提交保修', command=submit_repair).pack()


login_page = tk.Frame(root)
login_page.pack()

tk.Label(login_page, text='学号: ').grid(row=1, column=1)
username = tk.StringVar()
tk.Entry(login_page, textvariable=username).grid(row=1, column=2)

tk.Label(login_page, text='密码: ').grid(row=2, column=1, pady=10)
password = tk.StringVar()
tk.Entry(login_page, textvariable=password).grid(row=2, column=2)

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
    admin_dashboard_window.geometry('300x250')

    tk.Button(admin_dashboard_window, text="管理员登录", command=open_admin_login).pack()
    tk.Button(admin_dashboard_window, text="管理员注册", command=open_admin_register).pack()

    # 在这里添加管理员面板的功能，例如管理学生信息和维修请求等


# root = tk.Tk()
# root.title("主页面")


tk.Button(login_page, text='注册', command=open_register_page).grid(row=3, column=3, pady=10)
tk.Button(login_page, text='管理员页面', command=open_admin_dashboard).grid(row=4, column=2)

root.mainloop()

