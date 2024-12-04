import requests
import json
import simplejson
import base64
import tkinter as tk
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageTk
from PIL import ImageGrab
import time

class face_change():

    #第一步：获取人脸关键点
    def find_face(self, imgpath):
     """
     :param imgpath: 图片的地址
     :return: 一个字典类型的人脸关键点 如：{'top': 156, 'left': 108, 'width': 184, 'height': 184}
     """
     http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect' #获取人脸信息的接口
     data = {
     "api_key":"x2NyKaa6vYuArYwat4x0-NpIbM9CrwGU",#访问url所需要的参数
     "api_secret":"OuHx-Xaey1QrORwdG7QetGG5JhOIC8g7",#访问url所需要的参数
     "image_url":imgpath, #图片地址
     "return_landmark":1
     }


     files = {'image_file':open(imgpath,'rb')} #定义一个字典存放图片的地址
     response = requests.post(http_url,data=data,files=files)
     #print(response)
     res_con1 = response.content.decode('utf-8')
     res_json = simplejson.loads(res_con1)
     #print(res_json)
     faces = res_json['faces']
     list = faces[0]
     rectangle = list['face_rectangle']
     return rectangle


    #第二步：实现换脸
    def merge_face(self):
      """
      :param image_url1: 被换脸的图片路径
      :param image_url2: 换脸的图片路径
      :param image_url: 换脸后生成图片所保存的路径
      :param number: 换脸的相似度
      """
      #首先获取两张图片的人脸关键点
      number = 100
      face1 = self.find_face(self.path_image)
      face2 = self.find_face(self.path_image_1)
      #将人脸转换为字符串的格式
      rectangle1 = str(str(face1['top']) + "," + str(face1['left']) + "," + str(face1['width']) + "," + str(face1['height']))
      rectangle2 = str(str(face2['top']) + "," + str(face2['left']) + "," + str(face2['width']) + "," + str(face2['height']))
      #读取两张图片
      f1 = open(self.path_image,'rb')
      f1_64 = base64.b64encode(f1.read())
      f1.close()
      f2 = open(self.path_image_1, 'rb')
      f2_64 = base64.b64encode(f2.read())
      f2.close()

      url_add = 'https://api-cn.faceplusplus.com/imagepp/v1/mergeface' #实现换脸的接口
      data={
      "api_key": "x2NyKaa6vYuArYwat4x0-NpIbM9CrwGU",
      "api_secret": "OuHx-Xaey1QrORwdG7QetGG5JhOIC8g7",
      "template_base64":f1_64,
      "template_rectangle":rectangle1,
      "merge_base64":f2_64,
      "merge_rectangle":rectangle2,
      "merge_rate":number
      }
      response1 = requests.post(url_add,data=data)
      res_con1 = response1.content.decode('utf-8')
      res_dict = json.JSONDecoder().decode(res_con1)
      result = res_dict['result']
      #print(result)
      imgdata = base64.b64decode(result)
      #imgdata.save(image_url, 'jpg')
      self.save_image(imgdata)



    def open_image_1(self):
        global img
        self.path_image = askopenfilename(title="选择文件", initialdir="E://image")
        # path.set(path_image)
        self.image_open = Image.open(self.path_image)
        self.image_open = self.image_open.resize((336, 340))
        img = ImageTk.PhotoImage(self.image_open)
        self.face_label_1.config(image=img)
        pass
    def open_image_2(self):
        global img_1
        self.path_image_1 = askopenfilename(title="选择文件", initialdir="E://image")
        # path.set(path_image)
        self.image_open_1 = Image.open(self.path_image_1)
        self.image_open_1 = self.image_open_1.resize((337, 340))
        img_1 = ImageTk.PhotoImage(self.image_open_1)
        self.face_label_2.config(image=img_1)
        pass
    def open_image_3(self, path):
        image_save = Image.open(path)
        image_save.show()

    def save_image(self, imgdata):
        if self.image_save:
            rename = asksaveasfilename(title="保存文件", initialdir='E://image', filetype=[("PNG", ".png")])
            #print(rename)
            #self.image_open = self.add_text_to_image(self.image_open)

            if rename == '':
                tk.messagebox.showinfo('提示', '已取消保存！')
            else:
                file = open(rename, "wb")
                file.write(imgdata)
                file.close()
                tk.messagebox.showinfo(title="提示 ", message="保存成功！ ")
                self.open_image_3(rename)

        if self.image_save is None:
            tk.messagebox.showerror(title="错误", message="请先选择图片")
            pass
        pass
    def __init__(self):
        face_change_window = tk.Toplevel()
        face_change_window.geometry('800x533')
        face_change_window.title('AI换脸')
        face_change_window.iconbitmap('icon1.ico')
        self.image_save = './a1.gif'
        image_file = tk.PhotoImage(file='./800.gif')
        canvas = tk.Canvas(face_change_window, height=533, width=800)  # 创建画布
        image = canvas.create_image(0, 0, anchor='nw', image=image_file)  # 将图片置于画布上
        canvas.pack(side='top')

        self.face_label_1 = Label(face_change_window, bg='gray')
        self.face_label_1.place(x=39, y=65, width=336, height=340)
        self.face_label_2 = Label(face_change_window, bg='gray')
        self.face_label_2.place(x=426, y=65, width=337, height=340)

        face_button_1 = Button(face_change_window, bg='black', text='选择人像', fg='#FFFFFF', font=("华文楷体", 13),
                               command=self.open_image_1)
        face_button_1.place(x=148, y=455, w=117, h=41)
        face_button_2 = Button(face_change_window, bg='black', text='选择人像', fg='#FFFFFF', font=("华文楷体", 13),
                               command=self.open_image_2)
        face_button_2.place(x=536, y=455, w=118, h=40)

        face_change = Button(face_change_window, bg='black', text=' 执 行 ', fg='#FFFF99', font=("华文楷体", 13),
                             command=self.merge_face)
        face_change.place(x=341, y=455, w=117, h=41)

        face_change_window.mainloop()

#if __name__ == '__main__':
   #image1 = "D:\Python\python code/xue.jpg"
   #image2 = "D:\Python\python code/li.jpg"
   #image3 = "D:\Python\python code\image/face.jpg"
   #merge_face(image1, image2, image3, 100)
#face_change()