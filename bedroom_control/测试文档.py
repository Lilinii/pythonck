class Student:
    def __init__(self, name, student_id, password, dorm_number):
        self.name = name
        self.student_id = student_id
        self.password = password  # 注意：实际应用中应加密存储密码
        self.dorm_number = dorm_number

    def __str__(self):
        return f"Name: {self.name}, Student ID: {self.student_id}, Dorm Number: {self.dorm_number}"

# 存储学生信息的列表
students = []

# 添加学生信息的函数
def add_student(name, student_id, password, dorm_number):
    new_student = Student(name, student_id, password, dorm_number)
    students.append(new_student)

# 根据姓名或学号搜索学生的函数
def search_student(query):
    for student in students:
        if student.name == query or student.student_id == query:
            return student
    return None

# 示例：添加一些学生信息
add_student("张三", "123456", "password123", "Dorm1")
add_student("李四", "789101", "password456", "Dorm2")

# 示例：搜索学生
search_query = "张三"  # 或者使用学号 "123456"
found_student = search_student(search_query)

if found_student:
    print(found_student)
else:
    print("没有找到学生。")

