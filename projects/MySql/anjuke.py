import requests
import re
import pymysql

# 实战抓取安居客广西南宁全区的租房信息(正则表达式,数据库保存)
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


def insert_house_detail(url):
    print(url)
    # 连接数据库和添加数据
    conn = pymysql.connect(host='localhost', user='root', password='password', database='zufang', port=3306)
    cursor = conn.cursor()

    # 添加数据
    sql = """
    insert into house(id,title,img,price,payType,leaseType,houseType,address,detail) values(null,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    # 获取数据并添加到数据库
    response = requests.get(url, headers=headers)
    text = response.text
    title = re.findall(r'<h3\sclass="house-title">(.*?)</h3>', text, re.DOTALL)[0]
    img = re.findall(r'<div\sclass="img_wrap">.*?<img\sdata-src="(.*?)".*?>', text, re.DOTALL)[0]
    price = re.findall(r'<span\sclass="price">.*?<em>(.*?)</em>', text, re.DOTALL)[0]
    payType = re.findall(r'<span\sclass="type">(.*?)</span>', text, re.DOTALL)[0]
    leaseType = re.findall(r'<span\sclass="info">(.*?)</span>', text, re.DOTALL)[1]
    houseType = re.findall(r'<span\sclass="info">(.*?)</span>', text, re.DOTALL)[0]
    # houseType = re.findall(r'<ul.*?class="f14">.*?<span\sclass="c_888 mr_15">.*?<span>(.*?)</span>.*?</li>', text, re.DOTALL)[0].replace('                                ', '').replace('&nbsp;', '').strip()

    address = re.findall(r'<li\sclass="house-info-item l-width">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    detail_tag = re.findall(r'<div\sclass="auto-general">(.*?)</div>', text, re.DOTALL)[0]
    # 去掉抓取到标签和空格
    detail = re.sub('<.+?>', "", detail_tag).replace('                                ', '').strip()


    cursor.execute(sql, (title, img, price, payType, leaseType, houseType, address, detail))
    conn.commit()
    conn.close()


def parse_page(url):

    response = requests.get(url, headers=headers)
    text = response.text
    # 先获取url
    urls = re.findall(r'<div\sclass="zu-info">.*?<a.*?href="(.*?)".*?>.*?</a>', text, re.DOTALL)[1:-2]

    for index,url_tag in enumerate(urls):
        insert_house_detail(url_tag)


def main():
    for x in range(1,21):
        url = 'https://nn.zu.anjuke.com/fangyuan/p%s/' % x
        parse_page(url)


if __name__ == '__main__':
    main()