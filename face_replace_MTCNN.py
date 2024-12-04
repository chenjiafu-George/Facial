#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# ============================================
# @Time     : 2020/07/13 14:21
# @Author   : George
# @FileName : align_lfw.py
# ============================================

import os
import cv2
import numpy as np
import tensorflow as tf
import random
from PIL import Image

import data_utils
import detect_face


os.environ['CUDA_VISIBLE_DEVICES'] = '/gpu:1'
def do_align_lfw(input_file_path, output_file_path, model_file_path, model_name_list,
                 image_shape=(112, 112, 3), recursive=False, suffix_info_list=()):
    """

    :param input_file_path: 输入文件夹
    :param output_file_path: 输出文件夹
    :param model_file_path: 人脸检测模型文件夹
    :param model_name_list: 人脸检测模型文件名 list
    :param image_shape:
    :param recursive: 是否递归查看文件夹
    :param suffix_info_list: 后缀名 list, example: [".png", ".jpg"]
    :return:
    """

    print("detect_align_lfw_data.....")
    # 判断输出文件夹
    data_utils.make_file(output_file_path, remove_flag=True)

    minsize = 60
    threshold = [0.6, 0.85, 0.8]
    factor = 0.85

    # image_info_list_generator[(0, 'cosmos/000001.png', 0), (1, 'cosmos/000002.png', 0)]
    # image_info = (0, 'cosmos/000001.png', 0) ---> image_info[0] 为第几张图像
    # image_info[1] 为 input_file_path 目录下的该图像的相对路径
    # image_info[2] 为 input_file_path 目录下的文件夹的量化号
    #image_info_list_generator = data_utils.get_file_path_list(input_file_path, recursive, suffix_info_list)
    #print(image_info_list_generator)
    #print("image_path_list: {}".format(input_file_path))

    with tf.device('/gpu:0'):
        with tf.Graph().as_default():
            # gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=args.gpu_memory_fraction)
            # sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
            sess = tf.compat.v1.Session()
            with sess.as_default():
                p_net, r_net, o_net = detect_face.create_mt_cnn(sess, model_file_path, model_name_list)
                pass
            #p_net, r_net, o_net = detect_face.create_mt_cnn(model_file_path, model_name_list)
            pass
        pass

    n_rof_images_total = 0
    n_rof = np.zeros((5,), dtype=np.int32)
    face_count = 0


    print("-" * 100)
    # print("image_info: {}".format(image_info))
    image_path = input_file_path
    print("image_path: {}".format(image_path))

    if n_rof_images_total % 100 == 0:
        print("Processing {}, {}".format(n_rof_images_total, n_rof))
        pass

    n_rof_images_total += 1

    if not os.path.exists(image_path):
        print("image path: {} is not found".format(image_path))
        pass

    try:
        image = cv2.imread(image_path)
        #print(image)
        pass
    except (IOError, ValueError, IndexError) as e:
        print("{}: {}".format(image_path, e))
        pass
    else:
        image_channel = image.ndim
        if image_channel < 2:
            print("Unable to align {}, image dim error".format(image_path))
            pass

        if image_channel == 2:
            image = data_utils.gray_to_rgb(image)
            pass

        image = image[:, :, 0: 3]


        _minsize = minsize
        _landmark = None

        # 人脸检测
        bounding_boxes, points = detect_face.detect(image, _minsize, p_net, r_net, o_net, threshold, factor)
        #print(bounding_boxes)
        #print(points)
        #print(len(bounding_boxes))
        print("image_shape: {}".format(image.shape))
        #bound ing 像素点坐标值 最后一项是人脸概率值
        #print(bounding_boxes[0])

        #print(detect_box)

        print(len(bounding_boxes))
        count = len(bounding_boxes)
        for i in range(count):
            label = int(i+1)
            detect_box = bounding_boxes[i]
            detect_box = np.array(detect_box)
            color = None
            line_thickness=None
            tl = line_thickness or round(0.002 * (image.shape[0] + image.shape[1]) / 2) + 1
            color = color or [random.randint(0, 255) for _ in range(3)]
            c1, c2 = (int(detect_box[0]), int(detect_box[1])), (int(detect_box[2]), int(detect_box[3]))
            cv2.putText(image, str(label), (c1[0], c1[1] - 10), 0, tl / 3, [225, 255, 255], thickness=tl,
                        lineType=cv2.LINE_AA)

            detect_image = cv2.rectangle(image, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)

        #target_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # # image_shape: h, w, c
        #detect_image = target_image[int(detect_box[1]): int(detect_box[3]),
         #                            int(detect_box[0]): int(detect_box[2])]
            print("detect_image_shape: {}".format(detect_image.shape))
        #cv2.imshow("detect_image", detect_image)
        #cv2.waitKey(0)


        file_name = "{:04d}.png".format(face_count)
        output_path = os.path.join(output_file_path, file_name)
        print("output_path: {}".format(output_path))
        # print(target_file)
        cv2.imwrite(output_path, detect_image)
        face_count += 1

        if len(points) == 0:
            print("image_path: {}".format(image_path))
            #print(" 不存在")
        else:
            _landmark = points.T
            #print(_landmark)
            pass
        return output_path, bounding_boxes[0:4]
    pass
pass


def replace(self, image_path, replace_image, face_box, number):
    image = Image.open(image_path)
    image_new = Image.open(replace_image)
    region_list = []
    flag = True
    #while flag:

    # print(len(face_box))
    count = int(number)
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
            flag = False
            image.show()

        else:
            print("no")
            pass





    # print(region_list[0].size)


'''
if __name__ == "__main__":
    from datetime import datetime

    # 代码开始时间
    start_time = datetime.now()
    print("开始时间: {}".format(start_time))

    #input_data_path = "../data/align_input"
    #input_data_path = b"./images"
    #input_data_path = input_data_path.decode('ascii')
    image_path = './images/people_four.jpg'
    replace_path = './face_replace.jpg'
    #output_data_path = "../data/align_output"
    output_data_path = "./data/detect"
    model_file = "./models/detect_model"
    model_name = ["det1.npy", "det2.npy", "det3.npy"]
    img_shape = [112, 112, 3]
    recursive_flag = False
    suffix_list = [".png", ".jpg", ".jpeg"]

    output_path, face_box = do_align_lfw(image_path, output_data_path, model_file, model_name,
                 img_shape, recursive_flag, suffix_list)

    print(output_path)
    replace(image_path, replace_path, face_box, 1)

    # 代码结束时间
    end_time = datetime.now()
    print("结束时间: {}, 训练模型耗时: {}".format(end_time, end_time - start_time))
'''