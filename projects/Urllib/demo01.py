from urllib import request,parse
from http.cookiejar import CookieJar
import requests
from lxml import  etree

# 请求网站方法
# resp = request.urlopen('http://www.baidu.com')
# print(resp.read())

# 下载方法
# request.urlretrieve('http://img07.tooopen.com/images/20170316/tooopen_sy_201956178977.jpg','1.jpg')

# urlencode编码
# params = {'name':'张三', 'age':18,'green':'hello world'}
# result = parse.urlencode(params)
# print(result)

# urlencode编码网址编码实战
# url = 'http://www.baidu.com/s'
# params = {'wd':'刘德华'}
# qs = parse.urlencode(params)
# url = url +'?' +qs
# resp = request.urlopen(url)
# print(resp.read())

# parse_qs解码
# params = {'name':'张三', 'age':18,'green':'hello world'}
# qs = parse.urlencode(params)
# print(qs)
# result = parse.parse_qs(qs)
# print(result)


# urlparse和urlsplit 区别是urlparse多了一个params
# url = 'http://www.baidu.com/s;result?wd=python#1'  result就是params

# url = 'http://www.baidu.com/s?wd=python#1'
# result = parse.urlparse(url)
# result = parse.urlsplit(url)
# print('scheme',result.scheme)
# print('netloc',result.netloc)
# print('path',result.path)
# print('params',result.params)
# print('query',result.query)
# print('fragment',result.fragment)



# 实战拉钩网
# url = 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%85%A8%E5%9B%BD'
# url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
# resp = request.urlopen(url)
# print(resp.read())
# headers = {
#     'Referer':'https://www.lagou.com/jobs/list_python?px=default&city=%E5%85%A8%E5%9B%BD',
#     'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
# }
# data = {
#     'frist':'true',
#     'pn':1,
#     'kd':'python'
# }
# rep = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
# resp = request.urlopen(rep)
# print(resp.read().decode('utf-8'))

# 实战百思不得姐
# url = 'https://sou.zhaopin.com/?jl=489&kw=python&kt=3'
# resp = request.urlopen(url)
# print(resp.read().decode('utf-8'))


# 没有使用代理的
# url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

# 使用代理的
# 1. 使用ProxyHandler 传入代理构建一个handler
# handler = request.ProxyHandler({'http':'121.232.148.137:9000'})
# 2. 使用handler创建一个opener
# opener = request.build_opener(handler)
# 3. 使用opener发送一个请求
# resp = opener.open(url)
# print(resp.read())




# 1.不使用cookie去请求QQ空间
# other_url = 'https://user.qzone.qq.com/1075297352/4'
# headers = {
#     'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
#     'cookie':'x-stgw-ssl-info=47f27ead342c782c2487d75d7df1e323|0.107|1534746582.403|95|.|I|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|40000|h2|0; pgv_pvi=2072608768; RK=j4RQTTmxx1; ptcz=a424994ea2d2ac9b608d2ea22c349fa4dbb1baed783e26f6de43c61ba18ee491; pgv_pvid=5386010134; o_cookie=1945775580; pac_uid=1_1945775580; tvfe_boss_uuid=c9bb6a28844ba0d8; eas_sid=s1t5D2y8O9i587e2Z548I4Y5A8; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; _ga=GA1.2.1906719304.1529032488; qz_screen=1360x768; QZ_FE_WEBP_SUPPORT=1; ptui_loginuin=3227612361; pt2gguin=o1945775580; luin=o1945775580; pgv_info=ssid=s7169592608; pgv_si=s7945513984; _qpsvr_localtk=0.026468648729494504; uin=o1945775580; ptisp=cm; lskey=00010000e4dedbf8a4879227eb0b58efdfa40a3ee5c3ccd3aa3313ddd84d65f829624fd6fda3d26057fc19ba; skey=@kuNa2hCo2; p_uin=o1945775580; pt4_token=fRy-gNW-BUNvsxm3*SmUbooh206vHBZDdBQTbUhtbmM_; p_skey=f8M*xnWxlHMtDISgUZY2QUlS3jrDx---JJgOVqSSLm8_; Loading=Yes; welcomeflash=1945775580_82544; 1945775580_todaycount=0; 1945775580_totalcount=5575; cpu_performance_v8=11; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; x-stgw-ssl-info=1d522ec268f8671eac18bcf77cced7c6|0.074|1534746443.801|88|.|I|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|36500|h2|0; rv2=80B73EC779A7CF5BE88851085EF6A47A2AC7E2A371E79396BA; property20=A21FBD4A7EC1E41D2E743503AD24D9E9224E7304D6FC104A8E7611CA7316CEBB32A054017CFFDAEE; qzmusicplayer=qzone_player_1075297352_1534746583802'
# }
# rep = request.Request(url=other_url,headers=headers)
# resp = request.urlopen(rep)
# with open('kongjian.html','w',encoding='utf-8') as fp:
    # write函数必须写入一个str的数据类型
    # resp.read()读出来是一个bytes的数据类型
    # bytes -> encode -> str
    # str -> decode ->bytes
    # fp.write(resp.read().decode('utf-8'))

# print(resp.read().decode('utf-8'))


# 1 登录
# 1.1 创建一个cookiejar对象
cookiejar = CookieJar()
# 1.2 使用cookiejar创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3 使用上一步handler创建一个opener
opener = request.build_opener(handler)
# 1.4 使用opener发送登录请求获取cookie
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
data = {
    'u':'1945775580',
    'p':'Xiaoe520'
}
login_url = 'https://i.qq.com/?s_url=http%3A%2F%2Fuser.qzone.qq.com%2F1075297352%2F4'
req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
opener.open(req)



# 2. 访问个人主页
# other_url = 'https://user.qzone.qq.com/1075297352/4'
# 获取个人主页的时候不需要重新创建opener了，而应该用之前的opener，因为之前的opener已经包含了需要的cookie信息
# req = request.Request(other_url,headers=headers)
# resp = opener.open(req)
# with open('kongjian.html','w',encoding='utf-8') as fp:
#     fp.write(resp.read().decode('utf-8'))

# requests get方法
# p = {'wd':'中国'}
# response = requests.get('http://www.baidu.com/s?',params=p)
# print(type(response.text))
# print(response.text)


# requests post方法
# data = {
#     'first':'true',
#     'pn':'1',
#     'kn':'python'
# }
#
# headers = {
#     'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
# }
#
#
# response = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false',data=data,headers=headers)
# print(type(response.json()))
# print(response.json())



# requests 使用代理
# url = 'http://httpbin.org/ip'
# proxy = {
#     'http':'171.38.37.149:8123'
# }
# response = requests.get(url=url,proxies=proxy)
# print(response.text)


# requests 处理cookie信息
url = 'http://www.renren.com/PLogin.do'

data = {
    'u':'1945775580',
    'p':'Xiaoe520'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

session = requests.Session()
session.post(url, data=data, headers=headers)
response = session.get('http://www.renren.com/438635844/profile')
with open('qq.html', 'w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))
