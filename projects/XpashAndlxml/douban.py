import requests
from lxml import etree


# 1.将目标网站的页面抓取下来
headers = {
    'Host':'movie.douban.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer':'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&srcqid=2328577874318033697&tn=93006350_hao_pg&wd=douban&oq=%25E8%2585%25BE%25E8%25AE%25AF%25E6%258B%259B%25E8%2581%2598&rsv_pq=a5c9fad500032d39&rsv_t=c45fuFhfw1QXFIl989itMrzlcssxBzOrrVGSndzUMM1KcQQn7C8JY6zoz3pfqLSKLuTd0%2FO8&rqlang=cn&rsv_enter=1&inputT=5137&rsv_sug3=33&rsv_sug2=0&rsv_sug4=5138'
}

url = 'https://movie.douban.com/'
resp = requests.get(url=url,headers=headers)
text = resp.text
# 2.将抓取下来的数据根据一点的规则进行提取
parser = etree.HTMLParser(encoding='utf-8')
html = etree.HTML(text,parser=parser)
ul = html.xpath("//ul[@class='ui-slide-content']")[0]
lis = ul.xpath("./li")
positions = []
for li in lis:
    url = li.xpath(".//li[@class='poster']/a/@href")[0]
    payUrl = li.xpath(".//li[@class='ticket_btn']//a/@href")[0]
    img = li.xpath(".//img/@src")[0]
    title = li.xpath("@data-title")[0]
    release = li.xpath("@data-release")[0]
    rate = li.xpath("@data-rate")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]

    position = {
        'url':url,
        'payUrl':payUrl,
        'img':img,
        'title':title,
        'release':release,
        'rate':rate,
        'director':director,
        'actors':actors,
        'duration':duration,
        'region':region
    }

    positions.append(position)


print(positions)