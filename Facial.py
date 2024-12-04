import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pickle
import 爬取图片 as crawler
import 图片界面
import 图片界面3
import random
import pymysql
import os
import sys
os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')



#爬取图片.main()

#def Get_photo():
   # 爬取图片.main()


def Get_information(usr_name):
    crawler.BaiDu(usr_name)
    pass

def Required_information_photo(usr_name):
    图片界面.Photo(name=usr_name)

def middle_interface(name):
    window_middle = tk.Toplevel()
    window_middle.title("你好 " + name)
    window_middle.geometry("720x452")
    window_middle.iconbitmap('icon1.ico')

    crawler_gif = PhotoImage(file="crawler1.gif")
    p_gif = PhotoImage(file='p1.gif')
    ai_gif = PhotoImage(file='a1.gif')

    window_middle_canvas = tk.Canvas(window_middle, height=500, width=700)
    window_middle_canvas.pack(side='top')
    window_middle_image_file = tk.PhotoImage(file='middle.gif')
    # window_middle_image_file_1 = tk.PhotoImage(file='logo.gif')

    window_middle_canvas.create_image(0, 0, anchor='nw', image=window_middle_image_file)
    # window_middle_canvas.create_image(0, 0, anchor='nw', image=window_middle_image_file_1)

    entry_crawler = tk.Button(window_middle, image=crawler_gif, text="爬虫系统", bg='black', font=("华文楷体", 20),
                              cursor="arrow",
                              command=lambda: Get_information(entry_usr_name.get()))
    entry_crawler.place(x=62, y=225, width=150, height=150)
    # entry_crawler.place(x=450,y=110,w=125,h=125)
    entry_operation = tk.Button(window_middle, image=p_gif, text="图片操作", bg='black', font=("华文楷体", 20), cursor="arrow",
                                command=lambda: Required_information_photo(entry_usr_name.get()))
    entry_operation.place(x=288, y=225, width=150, height=150)
    entry_ai = tk.Button(window_middle, image=ai_gif, bg='black', cursor='arrow', command=图片界面3.face_change)
    entry_ai.place(x=517, y=225, width=150, height=150)

    window_middle.mainloop()

def connection_mysql():
    connect = pymysql.Connect(
        host='101.200.181.208',  # 本地服务器地址
        port=3306,  # 端口
        user='root',  # 用户名
        password='cjf200101',  # 密码
        db='usr_register',  # 数据库名称
        charset='utf8'  # 默认编码   带中文需使用utf8模式
    )
    #获取游标(指定获取的数据格式，这里设定返回元组 dict格式)
    return connect, connect.cursor()


def usr_login():
    def find_all(sql, data):
        connect, cursor = connection_mysql()    #连接mysql
        # print(cursor)
        cursor.execute(sql % data)  #执行指令
        #print(cursor)
        results = cursor.fetchall() #获取需要的所有信息
        #print(results)
        cursor.close()
        connect.close()
        return results      #返回默认元组格式

    def find(sql):
        connect, cursor = connection_mysql()
        cursor.execute(sql)
        result = cursor.fetchall()
        #print(result)
        connect.close()
        cursor.close()
        return result

    def find_password(sql, data):
        connect, cursor = connection_mysql()
        cursor.execute(sql % data)
        result = cursor.fetchone()  #获取一条信息
        #print(result)
        password = result[0]
        #print(result[0])
        connect.close()
        cursor.close()
        return password

    #获取用户输入的 usr_name 和usr_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    textx = usr_pwd.strip()
    usr_name_transfer = usr_name
    #print(usr_pwd)


    #name = 'George'
    sql_find = "SELECT name,password,confirm_password FROM usr_login WHERE name = '%s'"
    sql_find_name = "SELECT name FROM usr_login"
    sql_find_password = "SELECT password FROM usr_login WHERE name = '%s'"

    data = usr_name
    #print(data)
    result = find_all(sql_find, data)
    mysql_name = find(sql_find_name)
    #print(mysql_password)
    #print(usr_pwd)
    #for information in result:
     #   print(information[1])
    # print(information[1])

    #print(mysql_name)
    judge = 0
    no_exist_name = 1
    for name in mysql_name:
        judge = 1
        #print(name)
        #is_sign_up =None
        if usr_name in name:
            #首先判断 用户名是否存在数据库中 在获取密码
            mysql_password = find_password(sql_find_password, data)
            if usr_pwd == mysql_password:
                tk.messagebox.showinfo(title="你好 " + usr_name, message="欢迎使用！\n                 by George")
                #window.destroy()
                middle_interface(usr_name)
            elif textx == '':
                messagebox.showinfo("提示", "输入不能为空!")

            else:
                tk.messagebox.showerror(title="错误", message="输入密码错误!\n请重新输入!")


    is_sign_up = False
    #判断循环停止条件 需考虑全面 在或不在 都需要考虑在里面
    for mysql_name_index in mysql_name:
        if usr_name in mysql_name_index:
            #print(usr_name)
            no_exist_name = 0
            #print(no_exist_name)
    if no_exist_name == 1:
        is_sign_up = tk.messagebox.askyesno(title='提示', message='用户名不存在\n是否现在注册?')
    if is_sign_up:
        usr_sign_up(usr_name_transfer)
    else:
        pass
        '''
    #这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获
    #中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配
    try:                #使用with 语句 会自动关闭文件
        with open('usrs_info.pickle','rb') as usr_file:     #pickle模块 用来保存用户信息
            usrs_info = pickle.load(usr_file)
            print(usrs_info)
    except FileNotFoundError:
        #这里就是我们在没有读取到 usr_file 的时候，程序会创建一个 usr_file 这个文件，并将管理员的用户和密码写入
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    #如果用户名和密码匹配成功，登陆成功，并跳出弹窗
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:          #使用usrs_info[usr_name] 匹配之前创建用户对应的值，此处为字典的知识
            tk.messagebox.showinfo(title="你好 " + usr_name, message="欢迎使用！\n                 by George")
            #middle_interface(usr_name)
            #tk.messagebox.showinfo(title="欢迎 "+usr_name,message="Hello "+usr_name)
            is_sign_up = None
        #如果用户名匹配成功，而密码输入错误，则跳出报错弹窗
        else:
            tk.messagebox.showerror(title="错误",message="输入密码错误!\n请重新输入!")
            is_sign_up = None
    elif textx == '':
        messagebox.showinfo("提示", "输入不能为空!")
    #如果用户名不存在
    else:
        is_sign_up = tk.messagebox.askyesno(title='提示',message='用户名不存在\n是否现在注册?')
    #提示需不需要注册新用户
    if is_sign_up:
        usr_sign_up()
    else:
        pass
        '''
def usr_sign_up(name_transfer):
    def sign_to_George_Python():
        def find_all(sql, data):
            connect, cursor = connection_mysql()  # 连接mysql
            # print(cursor)
            cursor.execute(sql % data)  # 执行指令
            # print(cursor)
            results = cursor.fetchall()  # 获取需要的所有信息
            cursor.close()
            connect.close()
            return results  # 返回默认元组格式

        def find(sql):
            connect, cursor = connection_mysql()
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
            connect.close()
            cursor.close()
            return result

        def find_password(sql, data):
            connect, cursor = connection_mysql()
            cursor.execute(sql % data)
            result = cursor.fetchone()  # 获取一条信息
            password = result[0]
            print(result[0])
            connect.close()
            cursor.close()
            return password
        def find_confirm_password(sql, data):
            connect, cursor = connection_mysql()
            cursor.execute(sql % data)
            result = cursor.fetchone()  # 获取一条信息
            confirm_password = result[0]
            print(result[0])
            connect.close()
            cursor.close()
            return confirm_password

        def insert_information(sql_insert, insert_data):
            connect, cursor = connection_mysql()
            cursor.execute(sql_insert % insert_data)  # 执行
            connect.commit()  # 提交
            #print('成功插入', cursor.rowcount, '条数据！')
            connect.close()
            cursor.close()


        # 获取注册时所输入的信息
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        #这里是打开我们记录数据的文件，将注册信息读出
        no_exist_name = 1

        data = nn
        sql = "SELECT name,password FROM usr_login WHERE name = '%s'"
        sql_find_name = "SELECT name FROM usr_login "
        sql_find_password = "SELECT password FROM usr_login WHERE name = '%s'"
        sql_find_confirm_password = "SELECT confirm_password FROM usr_login WHERE name = '%s'"

        #information = find_all(sql, data)
        mysql_name = find(sql_find_name)
        #mysql_password = find_password(sql_find_password, data)
        #mysql_confirm_password = find_confirm_password(sql_find_confirm_password, data)

        for mysql_name_index in mysql_name:
            if nn in mysql_name_index:
                #print(nn)
                no_exist_name = 0

        if no_exist_name == 0:
            tk.messagebox.showerror(title='错误', message='用户名已存在!')
        elif np!= npf:
            tk.messagebox.showerror(title='错误', message='两次输入的密码不相同!\n请重试!')
        else:
            sql_insert = "INSERT INTO usr_login(name,password,confirm_password) VALUES('%s','%s','%s')"
            insert_data = (nn,np,npf)
            insert_information(sql_insert,insert_data)
            tk.messagebox.showinfo(title='恭喜', message='注册成功!')  # 使用数据库连接 可查看其他用户(想法)
            # 销毁窗口
            window_sign_up.destroy()
        '''
        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        #这里就是判断，如果两次密码输入不一致，提示错误
        if np != npf:
            tk.messagebox.showerror(title='错误',message='两次输入的密码不相同!\n请重试!')
        #如果用户名已经存在在我们的数据文件，提示已经注册过
        elif nn in exist_usr_info:
            tk.messagebox.showerror(title='错误',message='用户名已存在!')
        #最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功
        #然后销毁窗口
        else:
            exist_usr_info[nn] = npf
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)        #录入之前的信息表 和 现在的信息
            tk.messagebox.showinfo(title='恭喜',message='注册成功!')    #使用数据库连接 可查看其他用户(想法)
            #销毁窗口
            window_sign_up.destroy()
        '''
    def btn_sign_up_click(self):
        sign_to_George_Python()

    window_sign_up = tk.Toplevel(window)
    #window_sign_up.attributes("-alpha",1.5)    #半透明窗口
    window_sign_up.geometry("720x452")
    window_sign_up.title("注册")
    # 窗口基于屏幕的坐标
    window_sign_up.geometry("+512+200")
    window_sign_up.iconbitmap('icon1.ico')

    canvas_window_sign_up = tk.Canvas(window_sign_up, height=452, width=720)
    background_file_sign_up = tk.PhotoImage(file="register.gif")
    background_sign_up = canvas_window_sign_up.create_image(0, 0, anchor='nw', image=background_file_sign_up)
    canvas_window_sign_up.pack(side='top')  # 放置画布（为上端)

    #tk.Label(window_sign_up, text='欢 迎 注 册', font=("华文楷体", 20)).place(x=205, y=55)
    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    new_name.set(name_transfer)  # 默认值为 example@qq.com
    #tk.Label(window_sign_up, text='用户名:', font=("华文楷体", 15)).place(x=120, y=120)  # 将User name 放置在坐标（10，10）
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name, cursor="arrow", font=("华文楷体", 14),
                              relief="ridge", width=18, justify='center')
    entry_new_name.place(x=295, y=140, height=39)

    new_pwd = tk.StringVar()
    #tk.Label(window_sign_up, text='密码:', font=("华文楷体", 15)).place(x=120, y=170)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, cursor="arrow", font=("华文楷体", 14),
                             relief="ridge",
                             width=18, show="*", justify='center')  # 此处可以设置 单选框 来调整密码 是否需要隐藏显示
    entry_usr_pwd.place(x=295, y=207, height=39)

    new_pwd_confirm = tk.StringVar()
    #tk.Label(window_sign_up, text='确认密码:', font=("华文楷体", 15)).place(x=120, y=220)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, cursor="arrow", font=("华文楷体", 14),
                                     relief="ridge",
                                     width=18, show="*", justify='center')
    entry_usr_pwd_confirm.place(x=295, y=274, height=39)

    btn_confirm_sign_up = tk.Button(window_sign_up, text='注册', bg='black', fg='white', font=("华文楷体", 12), command=sign_to_George_Python)
    window_sign_up.bind('<Return>', btn_sign_up_click)
    btn_confirm_sign_up.place(x=302, y=339, width=118, height=40)

    window_sign_up.mainloop()

def usr_login_click(self):
    usr_login()

#随机数设置颜色 n
def background_tk():
    #gif_1 = PhotoImage(file="麋鹿7.gif")
    #button_image["image"] = gif_1
    #labelx["fg"] = "gold"
    #image_file_2 = tk.PhotoImage(file="麋鹿3.gif")
    #canvas.create_image(0, 0, anchor='nw', image=image_file_2)

    i=random.choice(range(14))+1
    #print(i)
    x = ["springgreen", "black", "gold", "royalblue", "lightblue","mediumpurple", "violet", "magenta", "tan","pink","orange","brown","coral","tomato","rosybrown"]
    labelx["fg"]=x[i]
    #print(x[i])

    '''
    x={"1": "green", "2": "black", "3": "gold", "4": "white", "5": "blue", "6": "purple"}
    for key in x:
        labelx["fg"]=x[key]
        print(x[key])
        pass
    '''

    '''
    for i in range(1,7):
        for i in ({"1":"green", "2":"black", "3":"gold", "4":"white", "5":"blue", "6":"purple"}):
            labelx["fg"] = dict["i"]
            '''
    pass

window = tk.Tk()
window.title("欢迎回来！")
window.geometry('720x452')  # 720x452
window.geometry('+470+150')
window.iconbitmap('icon1.ico')
image_file = tk.PhotoImage(file='background2.gif')  # 使用ps 导出即可 必须是原图片就是.gif文件
#image_file1 = tk.PhotoImage(file='麋鹿1.gif')

canvas = tk.Canvas(window, height=500, width=1000)  # 创建画布
image = canvas.create_image(0, 0, anchor='nw', image=image_file)  # 将图片置于画布上
canvas.pack(side='top')  # 放置画布（为上端)

#image1 = canvas.create_image(-130, -30, anchor='nw', image=image_file1)
# image1 = canvas.create_image(310,50,anchor='nw',image=image_file1)

#background_tk(window)

#labelx = tk.Label(window, text='用 户 登 录 ', font=("华文楷体", 20))
#labelx.place(x=405, y=105)
#tk.Label(window, text="用户名:", font=("华文楷体", 16)).place(x=310, y=190)
#tk.Label(window, text="密码:", font=("华文楷体", 16)).place(x=310, y=240)

#button_image_settings = Label(window, text='按钮图片设置：',fg="green")
#button_image_settings.place(x=600,y=0)

#gif = PhotoImage(file="金.gif")
#gif_1 = PhotoImage(file="麋鹿7.gif")

#button_image = Button(window, image=gif, text="点击", bd=5, command=lambda : background_tk())
#button_image.place(x=650,y=10,w=60,h=60)

var_usr_name = tk.StringVar()  # 定义变量
var_usr_name.set("George")  # 变量赋值'example@python.com'
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, cursor="arrow", font=("华文楷体", 15), relief='ridge',
                          bd=1, width=22)  # 创建一个`entry`，显示为变量`var_usr_name`即图中的`example@python.com`
entry_usr_name.place(x=282, y=143, height=46)
#282 22
var_usr_pwd = tk.StringVar()  # 定义变量
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, cursor="arrow", relief='ridge', bd=1, font=("华文楷体", 15),
                         show='*', width=22)  # `show`这个参数将输入的密码变为`***`的形式
entry_usr_pwd.place(x=282, y=209, height=46)

btn_login = tk.Button(window, text='登录', font=("华文楷体", 12), bg='#666666', fg='#FFFFFF', command=usr_login)
btn_login.place(x=295, y=275,width=132, height=47)
#绑定快捷键
window.bind("<Return>", usr_login_click)
btn_sign_up = tk.Button(window, text='立即注册', font=("华文楷体", 12), bg='#666666', fg='#FFFFFF', command=lambda: usr_sign_up(entry_usr_name.get()))
btn_sign_up.place(x=295, y=340, width=132, height=48)

window.mainloop()
