import requests
from bs4 import BeautifulSoup
import re

# 实战爬取驾考宝典全国驾校

BASE_URL = 'http://www.jiakaobaodian.com'
CAR_DATAS = []
CAR_DATA = {}


def parse_page(url):
    headers = {
        'Referer':'http://www.jiakaobaodian.com/school/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')


    # rankings = soup.find_all('div',class_='sort-w')
    # for ranking in rankings:
    #     CAR_DATA['rankingNum'] = ranking.string
    #     CAR_DATAS.append(CAR_DATA)
    #
    #
    #
    # evaluates = soup.select('div .address a')
    # for evaluate in evaluates:
    #     if evaluate.string.endswith('评论'):
    #         CAR_DATA['evaluateNum'] = evaluate.string
    #
    #     CAR_DATAS.append(CAR_DATA)
    # print(CAR_DATA)

    # BeautifulSoup4
    # soup = BeautifulSoup(text, 'lxml')
    # detail_urls = soup.find_all('a',class_='left img-w')
    # for detail_url in detail_urls:
    #     carDetailUrl = BASE_URL + detail_url['href']
    #     parse_detail_car(carDetailUrl)

    # re

    detail_urls = re.findall(r'<li\sclass="clearfix\s">.*?<a\sclass="left img-w".*?href="(.*?)".*?>.*?</a>', text, re.DOTALL)
    print(detail_urls)
    for detail_url in detail_urls:
        carDetailUrl = BASE_URL + detail_url
        parse_detail_car(carDetailUrl)


def parse_detail_car(url):
    headers = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    text = response.content.decode('utf-8')

    # soup = BeautifulSoup(text, 'lxml')
    # imgs = soup.find('img')['src']
    # CAR_DATA['imgs'] = imgs
    # names = soup.find('a',class_='title').string
    # CAR_DATA['names'] = names
    # starting = soup.find('span',class_='score').string
    # CAR_DATA['starting'] = starting
    # allStudents = soup.find('span',class_='student').string
    # CAR_DATA['allStudents'] = allStudents
    print(url)
    imgs = re.findall(r'<a\sclass="left\simg-w".*?>.*?<img.*?src="(.*?)".*?>.*?</a>', text, re.DOTALL)
    CAR_DATA['imgs'] = imgs[0]
    names = re.findall(r'<a\sclass="title".*?>(.*?)</a>', text, re.DOTALL)
    CAR_DATA['names'] = names[0]
    starting = re.findall(r'<span\sclass="score-w".*?>.*?<span\sclass="score".*?>(.*?)</span>.*?</span>', text, re.DOTALL)
    CAR_DATA['starting'] = starting[0]
    allStudents = re.findall(r'<span\sclass="student".*?>(.*?)</span>', text, re.DOTALL)
    CAR_DATA['allStudents'] = allStudents[0]
    positions = re.findall(r'<p\sclass="field".*?>(.*?)<span.*?</p>', text, re.DOTALL)
    if positions[0].startswith('驾校地址'):
        CAR_DATA['position'] = positions[0]
    prices = re.findall(r'<p\sclass="price".*?>(.*?)</p>', text, re.DOTALL)
    if len(prices) > 0:
        CAR_DATA['prices'] = prices[0]
    else:
        CAR_DATA['prices'] = '暂无价格'
    carContents = re.findall(r'<div\sclass="com-jiaxiao-introducea\scom-part".*?>.*?<div\sclass="content".*?>(.*?)</div>.*?</div>', text, re.DOTALL)
    CAR_DATA['carContent'] = carContents[0]
    CAR_DATAS.append(CAR_DATA)
    print(CAR_DATAS)
    # positions = soup.find('p',attrs={'class':'field'})
    # for position in positions:
    #     if position.string.startswith('驾校地址'):
    #         CAR_DATA['position'] = position
    #
    #
    # prices = soup.find('p',attrs={'class':'price'}).string
    # CAR_DATA['prices'] = prices
    # carContents = soup.find_all('div',attrs={'class':'content'})[4]
    # for carContent in carContents:
    #     CAR_DATA['carContent'] = carContent
    #
    # CAR_DATAS.append(CAR_DATA)
    # print(CAR_DATAS)


def main():
    urls = [
        'http://www.jiakaobaodian.com/beijing/school/{}f.html',
        'http://www.jiakaobaodian.com/chongqing/school/{}f.html',
        'http://www.jiakaobaodian.com/shanghai/school/{}f.html',
        'http://www.jiakaobaodian.com/tianjin/school/{}f.html',
        'http://www.jiakaobaodian.com/anhui/school/{}f.html',
        'http://www.jiakaobaodian.com/fujian/school/{}f.html',
        'http://www.jiakaobaodian.com/guangdong/school/{}f.html',
        'http://www.jiakaobaodian.com/guangxi/school/{}f.html',
        'http://www.jiakaobaodian.com/guizhou/school/{}f.html',
        'http://www.jiakaobaodian.com/gansu/school/{}f.html',
        'http://www.jiakaobaodian.com/hebei/school/{}f.html',
        'http://www.jiakaobaodian.com/heilongjiang/school/{}f.html',
        'http://www.jiakaobaodian.com/henan/school/{}f.html',
        'http://www.jiakaobaodian.com/hubei/school/{}f.html',
        'http://www.jiakaobaodian.com/hunan/school/{}f.html',
        'http://www.jiakaobaodian.com/hainansheng/school/{}f.html',
        'http://www.jiakaobaodian.com/jilin/school/{}f.html',
        'http://www.jiakaobaodian.com/jiangsu/school/{}f.html',
        'http://www.jiakaobaodian.com/jiangxi/school/{}f.html',
        'http://www.jiakaobaodian.com/liaoning/school/{}f.html',
        'http://www.jiakaobaodian.com/neimenggu/school/{}f.html',
        'http://www.jiakaobaodian.com/ningxia/school/{}f.html',
        'http://www.jiakaobaodian.com/qinghai/school/{}f.html',
        'http://www.jiakaobaodian.com/shxi/school/{}f.html',
        'http://www.jiakaobaodian.com/shandong/school/{}f.html',
        'http://www.jiakaobaodian.com/sichuan/school/{}f.html',
        'http://www.jiakaobaodian.com/shanxi/school/{}f.html',
        'http://www.jiakaobaodian.com/xizang/school/{}f.html',
        'http://www.jiakaobaodian.com/xinjiang/school/{}f.html',
        'http://www.jiakaobaodian.com/yunnan/school/{}f.html',
        'http://www.jiakaobaodian.com/zhejiang/school/{}f.html'
    ]
    for url in urls:
        for x in range(1, 6):
            base_url = url.format(x)
            parse_page(base_url)


if __name__ == '__main__':
    main()