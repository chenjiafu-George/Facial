# -*- coding: utf-8 -*-
#!/usr/bin/env python

import urllib
import requests
import base64
import json
#client_id 为官网获取的AK， client_secret 为官网获取的SK
client_id ='R8pjx3a8g0hjSuWeIEGftbT4'
client_secret ='Q9o1C2xO5CkZ1CivAC6cCmdgB9YNoRh2'

#获取token
def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    token_content = response.read()
    if token_content:
        token_info = json.loads(token_content)
        token_key = token_info['access_token']
    return token_key


# 植物识别，返回可能性最大的植物
# filename:图片名（本地存储包括路径）,plantnum展示的数量
def plant(filename, plantnum):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"

    # 二进制方式打开图片文件
    f = open(filename, 'rb')
    img = base64.b64encode(f.read())

    params = dict()
    params['image'] = img
    params['baike_num'] = plantnum
    params = urllib.parse.urlencode(params).encode("utf-8")
    # params = json.dumps(params).encode('utf-8')

    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        # print(content)
        content = content.decode('utf-8')
        #print(content)
        data = json.loads(content)
        result = data['result']
        #print(result)
        nums = min(plantnum, len(result))

        for i in range(0, nums):
            item = result[i]
            #print('名称:', item['name'])
            #print('可能性:', item['score'])
            baike_info = item['baike_info']
            #print('百科描述:', baike_info['description'])
            #print('百科链接:', baike_info['baike_url'])
            #print('百科图片:', baike_info['image_url'])

            score = round(item['score'], 2)
            return str(item['name']), str(score), str(baike_info['description'])[0:230], str(baike_info['baike_url']), str(baike_info['image_url'])
    # return landmark


#plant("D:/image/1.png", 1)
