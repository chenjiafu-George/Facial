import tkinter as tk
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageTk
from PIL import ImageGrab
from PIL import ImageDraw,ImageFont
from tkinter.scrolledtext import ScrolledText
#import plant_identify_1
import random
import time
#import face_replace_MTCNN
from tkinter.filedialog import *


#tk.messagebox.showinfo(title="你好 " + name, message="欢迎使用爬图助手!\n                             by George")
crawler = tk.Toplevel()
crawler.title("爬取图片")
crawler.geometry("720x552")
crawler.geometry("+512+200")
crawler.iconbitmap('icon1.ico')
crawler.resizable(width=False, height=False)
menubar = tk.Menu(crawler)
# filemenu = tk.Menu(menubar,tearoff = 0)
fmenu = tk.Menu(menubar)
for item in ['新建', '打开', '保存', '另存为']:
    fmenu.add_command(label=item)
menubar.add_cascade(label="文件", menu=fmenu)

canvas_crawler = tk.Canvas(crawler, height=452, width=752)
background_file = tk.PhotoImage(file="crawler.gif")
#image_crawler_file = tk.PhotoImage(file="麋鹿6.gif")
#image_crawler_file_1 = tk.PhotoImage(file="麋鹿2.gif")
#image_crawler_file_2 = tk.PhotoImage(file="麋鹿8.gif")

background = canvas_crawler.create_image(0, 0, anchor='nw', image=background_file)
# image_crawler = canvas_crawler.create_image(-70, -10, anchor='nw', image=image_crawler_file)
# image_crawler_1 = canvas_crawler.create_image(370, -10, anchor='nw', image=image_crawler_file_1)
#image_crawler_2 = canvas_crawler.create_image(220, 10, anchor='nw', image=image_crawler_file_2)

canvas_crawler.pack()  # 放置画布（为上端)
log = ScrolledText(crawler, wrap=WORD, height=7,width=95)

log.pack(side="bottom")
#tk.Label(self.crawler, text="图片爬虫系统", font=("华文楷体", 20)).place(x=215, y=120)
#tk.Label(self.crawler, text="图片类型:", font=("华文楷体", 16)).place(x=130, y=200)
#tk.Label(self.crawler, text="页数:", font=("华文楷体", 16)).place(x=130, y=250)
var_image_type = tk.StringVar()  # 定义变量
var_image_type.set("")  # 变量赋值'example@python.com'
entry_image_type = tk.Entry(crawler, textvariable=var_image_type, cursor="arrow", font=("华文楷体", 14),
                            relief="ridge",width=21, justify='center')
entry_image_type.place(x=290, y=127,height=39)

var_image_page = tk.IntVar  # 定义变量

entry_image_page = tk.Entry(crawler, textvariable=var_image_page, cursor="arrow", font=("华文楷体", 14),
                            relief="ridge",width=21, justify='center')
entry_image_page.place(x=290, y=207, height=40)

var_path = tk.StringVar()
var_path.set(value=self.file)
entry_path = tk.Entry(crawler, textvariable=var_path, cursor="arrow", font=('华文楷体', 14), relief='ridge', width=15, justify='center')
entry_path.place(x=290, y=287, height=39)


select = tk.Button(crawler, text='选择', font=('华文楷体', 12), width=4, fg='#FFFFFF', bg='#666666',command=lambda: self.file)
select.place(x=432, y=292, height=29)

# image_type = entry_image_type.get()
# image_page = int(entry_image_page.get())
# print(type(image_page))
# lambda 函数里面使用.get（）方法得到输入框的东西
start = tk.Button(crawler, text='开始', font=("华文楷体", 12), width=8, fg='#FFFFFF', bg='#666666',
                  command=lambda: self.Required_information(self.entry_image_type.get(), self.entry_image_page.get()))
start.place(x=249, y=358, height=40)
entry_del_all = tk.Button(crawler, text='清空', width=8, font=('华文楷体', 12), fg='black', bg='#666666', command=lambda:self.emptyLog)
entry_del_all.place(x=381, y=358, height=40)
#crawler.bind("<Return>", crawler_click)
# stop = tk.Button(crawler, text="stop",font=("Cambria", 12), command="break")
# stop.place(x=500,y=200)
start_time = time.time()  # 启动time()函数 获取启动时间


crawler.mainloop()