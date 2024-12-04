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
#import face_replace_MTCNN
import random
import time
path_image = './001.png'
image_open = Image.open(path_image)

if image_open is None:
    tk.messagebox.showerror("错误", "请先选择图片!")
else:
    base_img_3 = Image.open("background3.jpg")
    box = (111, 132, 691, 425)
    region = image_open.convert("RGBA")

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
            #base_img_3 = self.add_text_to_image(base_img_3)
            base_img_3.save(str(base_img_rename) + '.png', 'PNG')
            tk.messagebox.showinfo(title="提示 ", message="保存成功! ")
            base_img_3.show()
    else:
        tk.messagebox.showinfo('提示', '已取消保存！')