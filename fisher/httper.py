"""
    Created by 朝南而行 2018/12/5 16:36
"""
__author__ = '朝南而行'


# urllib
# requests 推荐使用
from urllib import request
import requests


# class HTTP 和 HTTP(object) python3无区别都是新式类
# python2 经典类和新式类
class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url=url)
        # 我们需要返回的内容
        # restful
        # json
        # http://t.yushu.im/v2/book/isbn/9787121277139
        # 成功和不成功的判断
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text


