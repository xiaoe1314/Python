"""
    Created by 朝南而行 2018/12/5 16:36
"""
import requests
import json
from multiprocessing import Queue


# 实战抓取豆果美食APP数据(引入队列)
# 创建队列
queue_lists = Queue()


def handel_request(url, data):
    headers = {
        "client": "4",
        "version": "6932.2",
        "device": "OPPO R11",
        "sdk": "22,5.1.1",
        "imei": "866174010401657",
        "channel": "zhuzhan",
        "mac": "40:A5:EF:D3:A4:6C",
        "resolution": "1280*720",
        "dpi": "1.5",
        # "android-id": " 40a5efd3a46c2350",
        # "pseudo-id": " fd3a46c235040a5e",
        "brand": "OPPO",
        "scale": "1.5",
        "timezone": "28800",
        "language": "zh",
        "cns": "3",
        "carrier": "CHINA+MOBILE",
        "imsi": "460074016523921",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36",
        "reach": "1",
        "newbie": "0",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        # "Cookie": " duid=58928990",
        "Host": "api.douguo.net",
        # "Content-Length": " 89",
    }

    resp = requests.post(url=url, headers=headers, data=data)
    return resp


def handle_index():
    url = 'http://api.douguo.net/recipe/flatcatalogs'
    data = {
        "client": "4",
        # "_session": "1551791174767866174010401657",
        # "v": "1551352576",
        "_vs": "2305",
    }
    resp = handel_request(url=url, data=data)
    index_response_dict = json.loads(resp.text)
    for index_item in index_response_dict['result']['cs']:
        for index_item_1 in index_item['cs']:
            for item in index_item_1['cs']:
                name_data = {
                    "client": "4",
                    # "_session": "1551796106507866174010401657",
                    "keyword": item['name'],
                    "order": "0",
                    "_vs": "400",
                }
                queue_lists.put(name_data)

                # print(name_data['keyword'])


def handle_foot_list(data):
    print('当前处理的食材是：' + data['keyword'])
    foot_list_url = 'http://api.douguo.net/recipe/v2/search/0/20'
    foot_list_resp = requests.post(url=foot_list_url, data=data)
    foot_response_dict = json.loads(foot_list_resp.text)
    for foot_item in foot_response_dict['result']['list']:
        foot_info = {}
        foot_info['shicai'] = data['keyword']


if __name__ == '__main__':
    handle_index()
    handle_foot_list(queue_lists.get())
    # print(queue_lists.qsize())


