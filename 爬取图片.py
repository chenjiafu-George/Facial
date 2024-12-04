import requests
from threading import Thread
import re
import time
import datetime
import hashlib
import tkinter as tk
from tkinter import messagebox
from tkinter import Tk
from tkinter import Button
from tkinter import INSERT
from tkinter import END
from tkinter import WORD
from tkinter import BOTH
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import *
import os
import sys


os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')

def override_where():
    """ overrides certifi.core.where to return actual location of cacert.pem"""
    # change this to match the location of cacert.pem
    return os.path.abspath("cacert.pem")


# is the program compiled?
if hasattr(sys, "frozen"):
    import certifi.core

    os.environ["REQUESTS_CA_BUNDLE"] = override_where()
    certifi.core.where = override_where

    # delay importing until after where() has been replaced
    import requests.utils
    import requests.adapters

    # replace these variables in case these modules were
    # imported before we replaced certifi.core.where
    requests.utils.DEFAULT_CA_BUNDLE_PATH = override_where()
    requests.adapters.DEFAULT_CA_BUNDLE_PATH = override_where()


class BaiDu():
    def __init__(self, name):
        #爬取百度图片
        tk.messagebox.showinfo(title="你好 " + name, message="欢迎使用爬图助手!\n                             by George")
        self.crawler = tk.Toplevel()
        self.crawler.title("爬取图片")
        self.crawler.geometry("720x552")
        self.crawler.geometry("+512+200")
        self.crawler.iconbitmap('icon1.ico')
        self.crawler.resizable(width=False, height=False)
        menubar = tk.Menu(self.crawler)
        # filemenu = tk.Menu(menubar,tearoff = 0)
        fmenu = tk.Menu(menubar)
        for item in ['新建', '打开', '保存', '另存为']:
            fmenu.add_command(label=item)
        menubar.add_cascade(label="文件", menu=fmenu)

        canvas_crawler = tk.Canvas(self.crawler, height=452, width=752)
        background_file = tk.PhotoImage(file="crawler.gif")
        #image_crawler_file = tk.PhotoImage(file="麋鹿6.gif")
        #image_crawler_file_1 = tk.PhotoImage(file="麋鹿2.gif")
        #image_crawler_file_2 = tk.PhotoImage(file="麋鹿8.gif")

        background = canvas_crawler.create_image(0, 0, anchor='nw', image=background_file)
        # image_crawler = canvas_crawler.create_image(-70, -10, anchor='nw', image=image_crawler_file)
        # image_crawler_1 = canvas_crawler.create_image(370, -10, anchor='nw', image=image_crawler_file_1)
        #image_crawler_2 = canvas_crawler.create_image(220, 10, anchor='nw', image=image_crawler_file_2)

        canvas_crawler.pack()  # 放置画布（为上端)
        self.log = ScrolledText(self.crawler, wrap=WORD, height=7,width=95)

        self.log.pack(side="bottom")
        #tk.Label(self.crawler, text="图片爬虫系统", font=("华文楷体", 20)).place(x=215, y=120)
        #tk.Label(self.crawler, text="图片类型:", font=("华文楷体", 16)).place(x=130, y=200)
        #tk.Label(self.crawler, text="页数:", font=("华文楷体", 16)).place(x=130, y=250)
        var_image_type = tk.StringVar()  # 定义变量
        var_image_type.set("")  # 变量赋值'example@python.com'
        self.entry_image_type = tk.Entry(self.crawler, textvariable=var_image_type, cursor="arrow", font=("华文楷体", 14),
                                    relief="ridge",width=21, justify='center')
        self.entry_image_type.place(x=290, y=127,height=39)

        var_image_page = tk.IntVar  # 定义变量
        self.entry_image_page = tk.Entry(self.crawler, textvariable=var_image_page, cursor="arrow", font=("华文楷体", 14),
                                    relief="ridge",width=21, justify='center')
        self.entry_image_page.place(x=290, y=207, height=40)

        var_image_page = tk.IntVar  # 定义变量

        self.entry_image_page = tk.Entry(self.crawler, textvariable=var_image_page, cursor="arrow", font=("华文楷体", 14),
                                    relief="ridge", width=21, justify='center')
        self.entry_image_page.place(x=290, y=207, height=40)

        self.var_path = tk.StringVar()

        entry_path = tk.Entry(self.crawler, textvariable=self.var_path, cursor="arrow", font=('华文楷体', 14), relief='ridge',
                              width=15, justify='center')
        entry_path.place(x=290, y=287, height=39)

        select = tk.Button(self.crawler, text='选择', font=('华文楷体', 12), width=4, fg='#FFFFFF', bg='#666666',
                           command=self.file)
        select.place(x=432, y=292, height=29)

        # image_type = entry_image_type.get()
        # image_page = int(entry_image_page.get())
        # print(type(image_page))
        # lambda 函数里面使用.get（）方法得到输入框的东西
        start = tk.Button(self.crawler, text='开始', font=("华文楷体", 12), width=8, fg='#FFFFFF', bg='#666666',
                          command=lambda: self.Required_information(self.entry_image_type.get(),
                                                                    self.entry_image_page.get()))
        start.place(x=249, y=358, height=40)
        entry_del_all = tk.Button(self.crawler, text='清空', width=8, font=('华文楷体', 12), fg='black', bg='#666666',
                                  command=lambda: self.emptyLog)
        entry_del_all.place(x=381, y=358, height=40)
        self.crawler.bind("<Return>", self.crawler_click)
        # stop = tk.Button(crawler, text="stop",font=("Cambria", 12), command="break")
        # stop.place(x=500,y=200)
        self.start_time = time.time()  # 启动time()函数 获取启动时间


        self.crawler.mainloop()

    def crawler_click(self, name):
        print(self)
        print(name)
        self.Required_information(name=self.entry_image_type.get(), page=self.entry_image_page.get())

    def Required_information(self, name, page):

        self.name = name
        self.page = page
        #print(type(self.page))
        # self.url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&rn=60&'
        self.url = 'https://image.baidu.com/search/acjson'
        # self.url = ''
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \         AppleWebKit/537.36 (KHTML, like Gecko) \         Chrome/35.0.1916.114 Safari/537.36',
            'Cookie': 'AspxAutoDetectCookieSupport=1'}
        self.num = 0
        Deal_image_type = name.strip()
        # Deal_image_page = page.strip()

        self.page_image = int(page)
        self.queryset()


    def queryset(self):
        #将字符串转换成查询字符串形式
        pn=0
        for i in range(int(self.page)):
            pn += 60*i                  #规定每次爬取的次数
            name = {
                'word':self.name,
                'pn':pn,
                'tn':'resultjson_com',
                'ipn':'rj',
                'rn':20
            }
            url = self.url
            self.getrequest(url, name)

    def getrequest(self, url, data):
        '''
        #发送请求
        print("[INFO]: 开始发送请求:"+url)
        ret = requests.get(url,headers=self.header,params=data)
        #访问限制
        if str(ret.status_code)=='200':
            print('[INFO]: request 200 ok :'+ret.url)
        else:
            print('[INFO]: request{},{}'.format(ret.status_code,ret.url))
        '''
        self.insertToLog("[INFO]: 开始发送请求:" + url)
        ret = requests.get(url, headers=self.header, params=data)
        print(ret)
        if str(ret.status_code) == '200':
            self.insertToLog('[INFO]: request 200 ok :' + ret.url)
        else:
            self.insertToLog('[INFO]: request{},{}'.format(ret.status_code, ret.url))
        response = ret.content.decode()
        print(response)
        img_links = re.findall(r'thumbURL.*?\.jpg',response)
        print(img_links)
        #img_name = re.findall(r'fromPageTitleEnc":".*?\,',response)

        links_url = []
        links_name = []
        #提取url
        for link in img_links:
            links_url.append(link[11:])
        #for link in img_name:
            #links_name.append(link[19:])
        boolean = self.thread(links_url)
        if boolean :
            tk.messagebox.showinfo(title="恭喜 ",
                               message="操作成功!\n共获得%d张图片." % (self.page_image * 20))
        else:
            pass

    def Saveimage(self, link, file):
        #保存图片
        self.insertToLog('[INFO]:正在保存图片：'+link)
        m = hashlib.md5()           #构造一个hashlib对象
        m.update(link.encode())     #对字符串进行解码 此处为 输入的 图片类型
        name = m.hexdigest()
        ret = requests.get(link,headers =self.header)
        image_content = ret.content             #存储图片信息
        filename = file + '/' + name +'.png'     #对应路径存储照片格式
        #print(filename)
        #写入文件
        with open(filename,'wb') as f:
            f.write(image_content)
        #保存成功
        self.insertToLog('[INFO]:保存成功，图片名为:{}.jpg'.format(name))

    def file(self):
        self.path = askdirectory(title="选择文件", initialdir="E://")
        self.var_path.set(value=self.path)
        #return path

    def thread(self,links):
        #多线程
        self.file = self.path
        if self.file == '':
            return False
            pass
        else:
            tk.messagebox.showinfo("提示", "正在下载图片...\n图片保存地址为:" + self.file)
            print(links)
            self.num +=1
            for i,link in enumerate(links):
                self.insertToLog('*'*50)
                self.insertToLog(link)
                self.insertToLog('*'*50)
                if link:                #延时0.5秒 防止服务器限制
                    time.sleep(0.5)
                    self.Saveimage(link, self.file)
                    #t = Thread(target=self.Saveimage(),args=(link,))
                    #t.start()
                    #t.join()
                self.num += 1
            self.insertToLog('一共进行了{}次请求'.format(self.num))

            return True


    #def stop(self,links):

    def insertToLog(self, str):
        self.log.insert(INSERT, str + '\n')
        self.log.see(END)

    def emptyLog(self):
        self.log.delete(0.0, END)
    def __del__(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #self.insertToLog("北京时间: " + now)

        end_time = time.time()
        #self.insertToLog('一共花费时间{}(单位秒)'.format(end_time-self.start_time))

#BaiDu('George')
'''
def main():
    name = input('请输入你要爬取的图片类型:')
    page = input('请输入你要爬取图片的页数(60张一页):')
    baidu = BaiDu(name,page)
    baidu.queryset()

if __name__ == '__main__':
    main()
'''










