import pymssql  # 导入模块

connect = pymssql.connect('LAPTOP-816947IA', 'sa', '12345678', 'TMS')
# connect = pymssql.connect('服务器名称', '用户名', '密码', '库名')  # 建立连接
if connect:
    print("连接成功")
