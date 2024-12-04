import tkinter as tk
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageTk
from PIL import ImageGrab
from PIL import ImageDraw,ImageFont
import plant_identify_1
import face_replace_MTCNN
import random
import time

#plant_identify_1.plant('D:\Python\python code/youcai.jpg', 1)
class Photo():
    # 添加水印
    def add_text_to_image(self, image):
        font = ImageFont.truetype('C:\Windows\Fonts\STXINGKA.TTF', 70)
        text = 'Facial'
        #image = self.image_open

        # 添加背景
        new_img = Image.new('RGBA', (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
        new_img.paste(image, image.size)

        # 添加水印
        font_len = len(text)
        rgba_image = new_img.convert('RGBA')
        text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 50))
        image_draw = ImageDraw.Draw(text_overlay)
        '''
        for i in range(0, rgba_image.size[0], font_len * 40 + 50):
            for j in range(0, rgba_image.size[1], 200):
                image_draw.text((i, j), text, font=font, fill=(0, 0, 0, 50))
        '''
        #获取文本大小
        text_size_x, text_size_y = image_draw.textsize(text, font=font)
        image_draw.text((rgba_image.size[0] * 2 / 3 - text_size_x - 30, rgba_image.size[1] * 2 / 3 - text_size_y - 30), text,
                        font=font, fill=(0, 0, 0, 100))
        text_overlay = text_overlay.rotate(0)
        image_with_text = Image.alpha_composite(rgba_image, text_overlay)

        # 裁切图片
        image_with_text = image_with_text.crop((image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2))
        return image_with_text

    def Open_photo(self):
        global img
        self.path_image = askopenfilename(title="选择文件", initialdir="D://image")
        #path.set(path_image)
        self.image_open = Image.open(self.path_image)
        img = ImageTk.PhotoImage(self.image_open)
        self.image_label.config(image=img)
        #image = Image.open(filename)
        #image.show()
        #self.image_label.image = img
    #图片裁剪
    def Clip_photo(self):
        #延时0.5秒 避免截取剪裁选项
        time.sleep(0.5)
        box=(150,190,950,920)
        im = ImageGrab.grab(box)
        im.show()

    #原路径保存
    def Save_photo(self):
        if self.path_image:
            self.image_open.save(self.path_image)
            tk.messagebox.showinfo(title="保存 ", message="保存成功 ")
        else:
            tk.messagebox.showerror(title="错误", message="请先选择图片")
            pass
    #指定路径保存
    def Save_as_photo(self):
        if self.path_image:
            rename = asksaveasfilename(title="保存文件", filetype=[("PNG", ".png")])
            print(rename)
            #self.image_open = self.add_text_to_image(self.image_open)

            if rename == '':
                tk.messagebox.showinfo('提示', '已取消保存！')
            else:
                tk.messagebox.showinfo(title="提示 " , message="保存成功！ ")
                self.image_open.save(str(rename) + '.png', 'PNG')
        if self.path_image is None:
            tk.messagebox.showerror(title="错误", message="请先选择图片")
            pass
    #旋转图片
    def Rotate_photo(self):
        #ImageTk.PhotoImage() 需要用global变量存储 旋转对Image.open()本身变量操作
        global img_rotate
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:

            image_new_width, image_new_hight = self.image_open.size  # 获取旋转后的图片大小
            # print(image_new_width,image_new_hight)
            if image_new_hight >= 500 and image_new_width >= 500:
                image_new_rotate = self.image_open.resize((image_new_width, image_new_hight))
            else:
                image_new_rotate = self.image_open.resize((500, 500))
            self.image_open = image_new_rotate.rotate(90)
            img_rotate = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_rotate)
        #self.image_open.show()
    #设置图片大小
    def Resize_photo(self):
        global img_resize
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = self.image_open.resize((500,500))
            #self.image_open.show()
            img_resize = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_resize)


    def Resize_photo_1(self):

        global img_resize_1
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = self.image_open.resize((800, 600))
            # self.image_open.show()
            img_resize_1 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_resize_1)

    def Resize_photo_2(self):

        global img_resize_2
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = self.image_open.resize((1024,768))
            img_resize_2 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_resize_2)
    #添加滤镜
    def Filter_photo(self):
        global img_filter
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = self.image_open.filter(ImageFilter.DETAIL)
            img_filter = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_filter)
    #模糊
    def Filter_photo_1(self):
        global img_filter_1
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = self.image_open.filter(ImageFilter.BLUR)
            img_filter_1 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_filter_1)
    #轮廓
    def Filter_photo_2(self):
        global img_filter_2
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = self.image_open.filter(ImageFilter.CONTOUR)
            img_filter_2 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_filter_2)
    #边界加强
    def Filter_photo_3(self):
        global img_filter_3
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = self.image_open.filter(ImageFilter.EDGE_ENHANCE)
            img_filter_3 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_filter_3)
    #平滑滤镜
    def Filter_photo_4(self):
        global img_filter_4
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = self.image_open.filter(ImageFilter.SMOOTH_MORE)
            img_filter_4 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_filter_4)
    #锐化滤镜
    def Filter_photo_5(self):
        global img_filter_5
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = self.image_open.filter(ImageFilter.SHARPEN)
            img_filter_5 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_filter_5)
    #还原
    def Filter_photo_restore(self):
        global img
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = Image.open(self.path_image)
            img = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img)
    #对比度
    def Contrast_photo(self):
        global img_contrast
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = ImageEnhance.Contrast(self.image_open).enhance(0.1)
            img_contrast = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_contrast)

    def Contrast_photo_1(self):
        global img_contrast_1
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = ImageEnhance.Contrast(self.image_open).enhance(0.5)
            img_contrast_1 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_contrast_1)

    def Contrast_photo_2(self):
        global img_contrast_2
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = ImageEnhance.Contrast(self.image_open).enhance(1.0)
            img_contrast_2 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_contrast_2)

    def Contrast_photo_3(self):
        global img_contrast_3
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = ImageEnhance.Contrast(self.image_open).enhance(1.5)
            img_contrast_3 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_contrast_3)

    def Contrast_photo_4(self):
        global img_contrast_4
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = ImageEnhance.Contrast(self.image_open).enhance(2.0)
            img_contrast_4 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_contrast_4)

    def Contrast_photo_restore(self):
        global img
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = Image.open(self.path_image)
            img = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img)
    #提高图片亮度
    def Up_bright_photo(self):
        global  img_up_bright
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.light = 1.1
            self.image_open = ImageEnhance.Brightness(self.image_open).enhance(self.light)
            img_up_bright = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_up_bright)

    def Low_bright_photo(self):
        global  img_low_bright
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.light = 0.9
            self.image_open = ImageEnhance.Brightness(self.image_open).enhance(self.light)
            img_low_bright = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_low_bright)
    #更换图片色彩
    def color_photo(self):
        global img_color
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = ImageEnhance.Color(self.image_open).enhance(0.1)
            img_color = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_color)

    def color_photo_1(self):
        global img_color_1
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            self.image_open = ImageEnhance.Color(self.image_open).enhance(1.5)
            img_color_1 = ImageTk.PhotoImage(self.image_open)
            self.image_label.config(image=img_color_1)
    #图片合成
    def compound_photo(self):
        if self.image_open is None:
            tk.messagebox.showerror("错误","请先选择图片!")
        else:
            base_img = Image.open("background.png")
            box = (335, 130, 640, 674)
            region = self.image_open.convert("RGBA")
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            base_img.paste(region,box)
            base_img.show()
            bool_photo = tk.messagebox.askokcancel('提示','是否保存图片')


            if bool_photo:
                base_img_rename = asksaveasfilename(title="保存文件", filetype=[("PNG", ".png")])
                #print(rename)
                #print(1)

                if base_img_rename == '':
                    tk.messagebox.showinfo('提示', '已取消保存！')
                else:
                    base_img = self.add_text_to_image(base_img)
                    base_img.save(str(base_img_rename) + '.png', 'PNG')
                    tk.messagebox.showinfo(title="提示 ", message="保存成功! ")
                    base_img.show()
            else:
                tk.messagebox.showinfo('提示', '已取消保存！')
                pass
        #是否保存
        #rename_base_img = asksaveasfilename(title="保存文件",filetype=[("PNG", ".png")])
        #base_img.save(str(rename_base_img) + '.png','PNG')

    def compound_photo_1(self):
        if self.image_open is None:
            tk.messagebox.showerror("错误","请先选择图片!")
        else:
            base_img_1 = Image.open("素材2.png")
            box = (156,57,643,543)
            region = self.image_open.convert("RGBA")

            region = region.resize((box[2] - box[0], box[3] - box[1]))
            base_img_1.paste(region,box)

            base_img_1.show()
            bool_photo = tk.messagebox.askokcancel('提示', '是否保存图片')
            if bool_photo:
                base_img_rename = asksaveasfilename(title="保存文件", filetype=[("PNG", ".png")])
                # print(rename)
                # print(1)

                if base_img_rename == '':
                    tk.messagebox.showinfo('提示', '已取消保存！')
                else:
                    base_img_1 = self.add_text_to_image(base_img_1)
                    base_img_1.save(str(base_img_rename) + '.png', 'PNG')
                    tk.messagebox.showinfo(title="提示 ", message="保存成功! ")
                    base_img_1.show()
            else:
                tk.messagebox.showinfo('提示', '已取消保存！')

    def compound_photo_2(self):
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            base_img_2 = Image.open("素材10.png")
            box = (40, 187, 757, 638)
            region = self.image_open.convert("RGBA")

            region = region.resize((box[2] - box[0], box[3] - box[1]))
            base_img_2.paste(region, box)

            base_img_2.show()
            bool_photo = tk.messagebox.askokcancel('提示', '是否保存图片')
            if bool_photo:
                base_img_rename = asksaveasfilename(title="保存文件", filetype=[("PNG", ".png")])
                # print(rename)
                # print(1)

                if base_img_rename == '':
                    tk.messagebox.showinfo('提示', '已取消保存！')
                else:
                    base_img_2 = self.add_text_to_image(base_img_2)
                    base_img_2.save(str(base_img_rename) + '.png', 'PNG')
                    tk.messagebox.showinfo(title="提示 ", message="保存成功! ")
                    base_img_2.show()
            else:
                tk.messagebox.showinfo('提示', '已取消保存！')

    def compound_photo_3(self):
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            base_img_3 = Image.open("素材9.png")
            box = (517, 49, 1525, 685)
            region = self.image_open.convert("RGBA")

            region = region.resize((box[2] - box[0], box[3] - box[1]))
            base_img_3.paste(region, box)

            base_img_3.show()
            bool_photo = tk.messagebox.askokcancel('提示', '是否保存图片')
            if bool_photo:
                base_img_rename = asksaveasfilename(title="保存文件", filetype=[("PNG", ".png")])
                # print(rename)
                # print(1)

                if base_img_rename == '':
                    tk.messagebox.showinfo('提示', '已取消保存！')
                else:
                    base_img_3 = self.add_text_to_image(base_img_3)
                    base_img_3.save(str(base_img_rename) + '.png', 'PNG')
                    tk.messagebox.showinfo(title="提示 ", message="保存成功! ")
                    base_img_3.show()
            else:
                tk.messagebox.showinfo('提示', '已取消保存！')
    def compound_photo_4(self):
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            base_img_3 = Image.open("background.jpg")
            box = (98, 37, 403, 339)
            region = self.image_open.convert("RGBA")

            region = region.resize((box[2] - box[0], box[3] - box[1]))
            base_img_3.paste(region, box)

            base_img_3.show()
            bool_photo = tk.messagebox.askokcancel('提示', '是否保存图片')
            if bool_photo:
                base_img_rename = asksaveasfilename(title="保存文件", filetype=[("PNG", ".png")])
                # print(rename)
                # print(1)

                if base_img_rename == '':
                    tk.messagebox.showinfo('提示', '已取消保存！')
                else:
                    base_img_3 = self.add_text_to_image(base_img_3)
                    base_img_3.save(str(base_img_rename) + '.png', 'PNG')
                    tk.messagebox.showinfo(title="提示 ", message="保存成功! ")
                    base_img_3.show()
            else:
                tk.messagebox.showinfo('提示', '已取消保存！')
    def compound_photo_5(self):
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            base_img_3 = Image.open("background1.jpg")
            box = (250, 70, 671, 620)
            region = self.image_open.convert("RGBA")

            region = region.resize((box[2] - box[0], box[3] - box[1]))
            base_img_3.paste(region, box)

            base_img_3.show()
            bool_photo = tk.messagebox.askokcancel('提示', '是否保存图片')
            if bool_photo:
                base_img_rename = asksaveasfilename(title="保存文件", filetype=[("PNG", ".png")])
                # print(rename)
                # print(1)

                if base_img_rename == '':
                    tk.messagebox.showinfo('提示', '已取消保存！')
                else:
                    base_img_3 = self.add_text_to_image(base_img_3)
                    base_img_3.save(str(base_img_rename) + '.png', 'PNG')
                    tk.messagebox.showinfo(title="提示 ", message="保存成功! ")
                    base_img_3.show()
            else:
                tk.messagebox.showinfo('提示', '已取消保存！')
    def compound_photo_6(self):
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            base_img_3 = Image.open("background2.jpg")
            box = (243, 173, 564, 665)
            region = self.image_open.convert("RGBA")

            region = region.resize((box[2] - box[0], box[3] - box[1]))
            base_img_3.paste(region, box)

            base_img_3.show()
            bool_photo = tk.messagebox.askokcancel('提示', '是否保存图片')
            if bool_photo:
                base_img_rename = asksaveasfilename(title="保存文件", filetype=[("PNG", ".png")])
                # print(rename)
                # print(1)

                if base_img_rename == '':
                    tk.messagebox.showinfo('提示', '已取消保存！')
                else:
                    base_img_3 = self.add_text_to_image(base_img_3)
                    base_img_3.save(str(base_img_rename) + '.png', 'PNG')
                    tk.messagebox.showinfo(title="提示 ", message="保存成功! ")
                    base_img_3.show()
            else:
                tk.messagebox.showinfo('提示', '已取消保存！')

    def compound_photo_7(self):
        if self.image_open is None:
            tk.messagebox.showerror("错误", "请先选择图片!")
        else:
            base_img_3 = Image.open("background3.jpg")
            box = (111, 132, 691, 425)
            region = self.image_open.convert("RGBA")

            region = region.resize((box[2] - box[0], box[3] - box[1]))
            base_img_3.paste(region, box)

            base_img_3.show()
            bool_photo = tk.messagebox.askokcancel('提示', '是否保存图片')
            if bool_photo:
                base_img_rename = asksaveasfilename(title="保存文件", filetype=[("PNG", ".png")])
                # print(rename)
                # print(1)

                if base_img_rename == '':
                    tk.messagebox.showinfo('提示', '已取消保存！')
                else:
                    base_img_3 = self.add_text_to_image(base_img_3)
                    base_img_3.save(str(base_img_rename) + '.png', 'PNG')
                    tk.messagebox.showinfo(title="提示 ", message="保存成功! ")
                    base_img_3.show()
            else:
                tk.messagebox.showinfo('提示', '已取消保存！')


    def compound_photo_self(self):
        global img
        self.background_image = askopenfilename(title="选择文件", initialdir="D://image")
        # path.set(path_image)
        self.image_background_open = Image.open(self.background_image)
        img_background = ImageTk.PhotoImage(self.image_background_open)
    #更换字体颜色
    def background_tk(self):
        # gif_1 = PhotoImage(file="麋鹿7.gif")
        # button_image["image"] = gif_1
        # labelx["fg"] = "gold"
        # image_file_2 = tk.PhotoImage(file="麋鹿3.gif")
        # canvas.create_image(0, 0, anchor='nw', image=image_file_2)

        i = random.choice(range(14)) + 1
        # print(i)
        x = ["springgreen", "black", "gold", "royalblue", "lightblue", "mediumpurple", "violet", "magenta", "tan",
             "pink", "orange", "brown", "coral", "tomato", "rosybrown"]
        self.b1["fg"] = x[i]
        # print(x[i])

    def plant_identify(self):
        tk.messagebox.showinfo(title="植物识别 ", message="正在识别中...\n   请耐心等待10-15s.")
        name, likely, description, description_url, picture_url = plant_identify_1.plant(self.path_image, 1)
        #print(name)
        if name == '非植物':
            tk.messagebox.showinfo('提示', '未检测到图中存在植物.')
        else:
            bool_photo = tk.messagebox.askokcancel('提示', '检测到' + name + '.\n是否了解详情?')
            if bool_photo:
                if name == '非植物':
                    tk.messagebox.showerror('错误', '暂未开放其他百科\n请联系管理员更新...')
                    pass
                else:
                    plant_encyclopedia = tk.Toplevel()
                    plant_encyclopedia.geometry('750x700')
                    plant_encyclopedia.title('植物百科')
                    plant_encyclopedia.iconbitmap('icon1.ico')
                    #image_file = tk.PhotoImage(file='B.gif')  # 使用ps 导出即可 必须是原图片就是.gif文件
                    # image_file1 = tk.PhotoImage(file='麋鹿1.gif')

                    #canvas = tk.Canvas(plant_encyclopedia, height=500, width=1000)  # 创建画布
                    #image = canvas.create_image(0, 0, anchor='nw', image=image_file)  # 将图片置于画布上
                    #canvas.pack(side='top')  # 放置画布（为上端)
                    image_label = Label(plant_encyclopedia, bg='grey')
                    image_label.place(x=0, y=0, width=750, height=400)

                    self.b1 = tk.LabelFrame(plant_encyclopedia, width=700, height=300, text=' 百 科 全 书 ', font=('华文楷体', 15),
                                       padx=10)
                    # b1.grid(padx=10,side='bottom')
                    self.b1.pack(padx=10, expand="no", side='bottom')

                    name_label = tk.Label(self.b1, text=' 名 称 : \t' + name, font=('华文楷体', 13))
                    # name_label.grid()
                    # name_label.grid(column=0, row=0)
                    name_label.place(x=200, y=0)
                    likely_label = tk.Label(self.b1, text=' 相似度 : ' + likely, font=('华文楷体', 13))
                    # likely_label.grid()
                    likely_label.place(x=200, y=30)
                    information_label = tk.Label(self.b1, text='百科描述 : ' + description[0:210], font=('华文楷体', 13), wraplength=600)
                    # information_label.grid()
                    information_label.place(x=30, y=60)
                    information_url_label = tk.Label(self.b1, text='百科链接 : ' + description_url, textvariable=description_url,
                                                     font=('华文楷体', 13))
                    #print(len(description))
                    # information_url_label.grid()
                    information_url_label.place(x=30, y=210)
                    picture_url_label = tk.Label(self.b1, text='图片链接 : ' + picture_url, font=('华文楷体', 13))
                    # picture_url_label.grid()
                    picture_url_label.place(x=30, y=240)
                    image_open = self.image_open.resize((750, 400))
                    global img
                    img = ImageTk.PhotoImage(image_open)
                    image_label.config(image=img)


        pass



    def self_information(self):
        tk_information = tk.Toplevel()
        tk_information.title("George个人信息♥")
        tk_information.geometry("+1100+0")
        tk_information.iconbitmap('icon1.ico')
        # lab3 = Label(tk2,text="你好，我叫George!",fg="green",back="black",font=("华文行楷",30))
        # lab3.grid(row=0,column=0)
        lab4 = Label(tk_information, text="你好，我叫George!\n年龄:19\n爱好:吉他、篮球\n个性签名:要么出局，要么出众!\n本人原创作品，请多关照。", fg="cyan", back="black",
                     font=("华文行楷", 20))
        lab4.grid(row=1, column=0)
        #time.sleep(5)
        tk_information.mainloop()
        pass

    def contact_author(self):
        image = Image.open("名片1.png")
        image.show()

    def open_image(self):
        self.replace_image = askopenfilename(title="选择文件", initialdir="E://image")
        image_new = Image.open(self.replace_image)
        #image_new.show()

    def replace(self, image_path, replace_image, face_box, number):
        #image.save(str(self.base_img_rename), 'PNG')
        image = Image.open(image_path)

        image_new = Image.open(replace_image)
        region_list = []
        flag = True
        while flag:

        # print(len(face_box))
            count = int(self.entry_image_index.get())
            if count == 0:
                flag = False
            for i in range(len(face_box)):
                if int(i + 1) == count:
                    box = face_box[i]
                    box = (int(box[0]), int(box[1]), int(box[2]), int(box[3]))
                    print(box)
                    # 将表情包图片转换成RGBA的模式
                    region = image_new.convert('RGBA')
                    # 将表情包图片的大小置为人脸框的大小
                    region = region.resize((int(box[2] - box[0]), int(box[3] - box[1])))
                    region_list.append(region)

                    # 将表情包粘到图片对应的人脸上
                    image.paste(region, box, region)
                    image.save(str(self.path_image_copy), 'PNG')
                    flag = False
                    image.show()

                else:
                    print("no")
                    pass

    def image_replace(self):
        if int(self.entry_image_index.get()) > 0 :
            self.replace(self.path_image_copy, self.replace_image, self.box,
                                       number=self.entry_image_index.get())
        pass

    def face_replace(self):
        tk.messagebox.showinfo(title="人脸检测 ", message="正在检测中...\n   请耐心等待1s.")
        #self.path_image = askopenfilename(title="选择文件", initialdir="E://image")
        # print(self.path_image)
        # print(self.path_image[:-3])
        # print(self.path_image[:-4])
        # copy
        if self.path_image[-4:] == 'jpeg' or self.path_image[-4:] == 'JPEG':
            self.path_image_copy = self.path_image[:-5] + '_copy' + '.png'
            print(self.path_image_copy)
        elif self.path_image[-4:] == '.jpg' or self.path_image[-4:] == '.JPG':
            self.path_image_copy = self.path_image[:-4] + '_copy' + '.jpg'
            print(self.path_image_copy)
        elif self.path_image[-4:] == '.png' or self.path_image[-4:] == '.PNG':
            self.path_image_copy = self.path_image[:-4] + '_copy' + '.png'
            print(self.path_image_copy)
        # print(self.path_image_copy)
        self.image_copy = Image.open(self.path_image)
        self.image_copy.save(str(self.path_image_copy), 'PNG')

        output_data_path = "./data/detect"
        model_file = "./models/detect_model"
        model_name = ["det1.npy", "det2.npy", "det3.npy"]
        self.base_img_rename = './0000.png'
        img_shape = [112, 112, 3]
        recursive_flag = False
        suffix_list = [".png", ".jpg", ".jpeg"]
        self.output_path, self.box = face_replace_MTCNN.do_align_lfw(self.path_image, output_data_path, model_file,
                                                                     model_name,
                                                                     img_shape, recursive_flag, suffix_list)
        face_replace = tk.Toplevel()
        face_replace.geometry('804x643')
        face_replace.title('人脸专区')
        face_replace.iconbitmap('icon1.ico')
        image_file = tk.PhotoImage(file='./5.gif')

        canvas = tk.Canvas(face_replace, height=643, width=804)  # 创建画布
        image = canvas.create_image(0, 0, anchor='nw', image=image_file)  # 将图片置于画布上
        canvas.pack(side='top')
        image_label = Label(face_replace, bg='grey')
        image_label.place(x=197, y=68, width=411, height=458)

        var_image_type = tk.StringVar()  # 定义变量
        var_image_type.set("")  # 变量赋值'example@python.com'
        self.entry_image_index = tk.Entry(face_replace, textvariable=var_image_type, cursor="arrow", font=("华文楷体", 14),
                                          relief="ridge", width=10, justify='center')
        self.entry_image_index.place(x=658, y=331, height=35)

        face_button_1 = Button(face_replace, bg='#666666', text='表情包', fg='#FFFFFF', font=("华文楷体", 13),
                               command=self.open_image)
        face_button_1.place(x=175, y=560, w=149, h=48)
        face_button_2 = Button(face_replace, bg='#666666', text=' 执 行 ', fg='#FFFF99', font=("华文楷体", 13),
                               command=self.image_replace)
        face_button_2.place(x=479, y=560, w=149, h=48)
        self.image = Image.open(self.output_path)
        self.image = self.image.resize((411, 458))
        global img
        img = ImageTk.PhotoImage(self.image)
        image_label.config(image=img)
        face_replace.mainloop()



    def __init__(self,name):
        tk.messagebox.showinfo(title="你好 "+name, message="欢迎进入图片操作系统！\n                 by George")
        window_image_operate = tk.Toplevel()
        window_image_operate.geometry("700x600")
        window_image_operate.geometry("+100+100")
        window_image_operate.title("图片操作")
        window_image_operate.iconbitmap('icon1.ico')
        self.path_image = None
        self.image_open = None
        window_image_operate_canvas = tk.Canvas(window_image_operate, height=600, width=700)  # 创建画布
        window_image_operate_canvas.pack(side='top')
        '''
        window_image_operate_canvas = Canvas(window_image_operate, height=600, width=700)
        image_file = tk.PhotoImage(file="background3.gif")
        image = window_image_operate_canvas.create_image(0, 0, anchor='nw', image=image_file)
        window_image_operate_canvas.pack(side='top')
        self.path_image = None
        '''
        menubar = Menu(window_image_operate)
        fmenu = Menu(menubar, tearoff=False)           #第一栏
        size_menu = Menu(menubar, tearoff=False)       #调整大小
        smenu = Menu(menubar, tearoff=False)           #第二栏
        tmenu = Menu(menubar, tearoff=False)           #第三栏
        light_menu = Menu(menubar, tearoff=False)      #亮度栏
        nmenu = Menu(menubar, tearoff=False)           #第四栏
        bmenu = Menu(menubar, tearoff=False)           #第五栏
        emenu = Menu(menubar, tearoff=False)           #第六栏
        identify_menu = Menu(menubar, tearoff=False)   #识别栏
        face_menu = Menu(menubar, tearoff=False)       #人脸栏

        fmenu.add_command(label = "打开",command=self.Open_photo)
        fmenu.add_command(label = "剪裁",command=self.Clip_photo)
        fmenu.add_command(label = "保存",command =self.Save_photo)
        fmenu.add_command(label = "另存为",command =self.Save_as_photo)

        size_menu.add_command(label='500x500',command=self.Resize_photo)
        size_menu.add_command(label='800x600', command=self.Resize_photo_1)
        size_menu.add_command(label='1024x800', command=self.Resize_photo_2)
        size_menu.add_command(label='还原', command=self.Filter_photo_restore)

        light_menu.add_command(label='增强', command=self.Up_bright_photo)
        light_menu.add_command(label='减弱', command=self.Low_bright_photo)
        light_menu.add_command(label='还原', command=self.Filter_photo_restore)

        smenu.add_command(label = "滤镜1（推荐）",command = self.Filter_photo)
        smenu.add_command(label = "滤镜2",command = self.Filter_photo_1)
        smenu.add_command(label = "滤镜3",command = self.Filter_photo_2)
        smenu.add_command(label="滤镜4", command=self.Filter_photo_3)
        smenu.add_command(label="滤镜5（推荐）", command=self.Filter_photo_4)
        smenu.add_command(label="滤镜6（推荐）", command=self.Filter_photo_5)
        smenu.add_command(label="还原", command=self.Filter_photo_restore)

        tmenu.add_command(label="0.1",command = self.Contrast_photo)
        tmenu.add_command(label="0.5", command=self.Contrast_photo_1)
        tmenu.add_command(label="1.0", command=self.Contrast_photo_2)
        tmenu.add_command(label="1.5（推荐）", command=self.Contrast_photo_3)
        tmenu.add_command(label="2.0", command=self.Contrast_photo_4)
        tmenu.add_command(label="还原", command=self.Contrast_photo_restore)

        nmenu.add_command(label="黑白", command=self.color_photo)
        nmenu.add_command(label="真彩（推荐）", command = self.color_photo_1)

        bmenu.add_command(label="模板1（竖版图片）", command=self.compound_photo)
        bmenu.add_command(label="模板2（竖版图片）", command=self.compound_photo_1)
        bmenu.add_separator()
        bmenu.add_command(label="模板3（横板图片）", command=self.compound_photo_2)
        bmenu.add_command(label="模板4（横板图片）", command=self.compound_photo_3)
        bmenu.add_separator()
        bmenu.add_command(label="家庭壁画", command=self.compound_photo_4)
        bmenu.add_command(label='家庭壁画2', command=self.compound_photo_5)
        bmenu.add_command(label='家庭壁画3', command=self.compound_photo_6)
        bmenu.add_command(label='家庭壁画4', command=self.compound_photo_7)
        bmenu.add_command(label="自定义模板", command=self.compound_photo_self)

        identify_menu.add_command(label='植物识别', command=self.plant_identify)
        face_menu.add_command(label='人脸遮挡', command=self.face_replace)

        emenu.add_command(label="版权信息", command=self.self_information)
        emenu.add_command(label="联系作者", command=self.contact_author)


        menubar.add_cascade(label = "文件",menu=fmenu)
        menubar.add_cascade(label="大小", menu=size_menu)
        menubar.add_cascade(label = "滤镜",menu=smenu)
        menubar.add_cascade(label='亮度', menu=light_menu)
        menubar.add_cascade(label = "对比度",menu = tmenu)
        menubar.add_cascade(label = "饱和度",menu = nmenu)
        menubar.add_cascade(label = "图片合成", menu = bmenu)
        menubar.add_cascade(label='识别', menu=identify_menu)
        menubar.add_cascade(label='人脸专区', menu=face_menu)

        menubar.add_cascade(label = "帮助",menu = emenu)
        window_image_operate.config(menu = menubar)

        #path = StringVar()
        #file_entry = Entry(window_image_operate, state='readonly', text=path)
        #file_entry.pack()

        self.image_label = Label(window_image_operate, bg = 'grey')
        self.image_label.place(x=0, y=0,width = 700, height = 600)
        '''
        size_label = Label(window_image_operate,text="更改图片大小：",font=("华文楷体",16))
        size_label.place(x=530,y=30)
        v=IntVar()
        resize_image = Radiobutton(window_image_operate,variable=v,text="500 x 500",value=1,command=self.Resize_photo)
        resize_image.place(x=555,y=70)
        resize_image_1 = Radiobutton(window_image_operate,variable=v,text="800 x 600",value=2,command = self.Resize_photo_1)
        resize_image_1.place(x=555,y=90)
        resize_image_2 = Radiobutton(window_image_operate,variable=v,text="1024 x 768",value=3,command = self.Resize_photo_2)
        resize_image_2.place(x=555,y=110)
        resize_image_restore = Radiobutton(window_image_operate, variable=v, text="还原", value=4,command=self.Filter_photo_restore)
        resize_image_restore.place(x=555, y=130)
        '''



        #for i in [self.Resize_photo,self.Resize_photo_1,self.Resize_photo_2]:
         #   Radiobutton(window_image_operate, variable=v, text="500 x 500", value=j, command=i).place(x=550,y=10+s)
          #  s += 20


        self.light = 1.0
        '''
        light_label = Label(window_image_operate, text="调整图片亮度：", font=("华文楷体", 16))
        light_label.place(x=530, y=190)
        up_light_btn = tk.Button(window_image_operate, text="增强", command=self.Up_bright_photo)
        up_light_btn.place(x=530, y=230, w=55, h=30)
        low_light_btn = tk.Button(window_image_operate, text="减弱", command=self.Low_bright_photo)
        low_light_btn.place(x=610, y=230, w=55, h=30)
        restore_btn = tk.Button(window_image_operate, text="还原", command=self.Filter_photo_restore)
        restore_btn.place(x=570,y=270,w=55,h=30)
        compound_btn = tk.Button(window_image_operate, text="植物识别", command=self.plant_identify)
        compound_btn.place(x=550, y=380, w=105, h=40)
        '''
        #image_btn = tk.Button(window_image_operate,text="选择图片",command=self.Open_photo)
        #image_btn.place(x = 70, y = 530,w = 150, h = 40)
        turn_gif = PhotoImage(file='turn1.gif')
        rotate_btn = tk.Button(window_image_operate, image=turn_gif, text="旋转", bg='black',command=self.Rotate_photo)
        rotate_btn.place(x=653, y=0)

        #save_btn = tk.Button(window_image_operate, text="保存", command=self.Save_photo)
        #save_btn.place(x=470, y=530, w=150, h=40)
        window_image_operate.mainloop()


#Photo(name="George")