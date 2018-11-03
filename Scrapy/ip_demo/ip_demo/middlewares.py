# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64


# 私密代理
class IpProxyDownloadMiddleware(object):
    PROXYS = ["115.223.227.122:9000", "183.230.162.20:8060"]

    def process_request(self, request, spider):
        proxy = random.choice(self.PROXYS)

        # raise SchemeNotSupported("Unsupported scheme: %r" % (uri.scheme,))
        # twisted.web.error.SchemeNotSupported: Unsupported scheme: b''
        # 出现这个问题,在前面加  'HTTP://'
        request.meta['proxy'] = 'HTTP://' + proxy

# 独享代理
# class IpProxyDownloadMiddleware(object):
#     def process_request(self, request, spider):
#         proxy = '183.230.162.20:8060'
#         user_password = "12345678:zz123456"
#         # raise SchemeNotSupported("Unsupported scheme: %r" % (uri.scheme,))
#         # twisted.web.error.SchemeNotSupported: Unsupported scheme: b''
#         # 出现这个问题,在前面加  'HTTP://'
#         request.meta['proxy'] = 'HTTP://' + proxy
#         b64_user_password = base64.b64encode(user_password.encode('utf-8'))
#         # 'Basic ' 后面有空格
#         request.headers['Proxy-Authorization'] = 'Basic ' + b64_user_password.decode('utf-8')


























