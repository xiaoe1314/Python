import requests
import re
import json

# 正则表达式实战抓取古诗文网页


def parse_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    text = response.text
    # <div\sclass="cont"> 某个div下面
    # .* 多个任意字符  . 点号不能匹配到 \n 在后面加 re.DOTALL 可以让 . 点号匹配所有字符
    # 匹配个字符需要非贪婪模式 加 ?
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    dynasties = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_tags = re.findall(r'<div\sclass="contson"\s.*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in content_tags:
        x = re.sub('<.*?>','',content)
        contents.append(x.strip())

    peoms = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        peom = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'content':content
        }
        peoms.append(peom)

    print("="*200)
    print(peoms)
    print("=" * 200)
    # json_peoms = json.dumps(peoms)
    # print(json_peoms.encode('utf-8').decode('utf-8'))


def main():
    # base_url = 'https://www.gushiwen.org/default_{}.aspx'
    # for x in range(1,100):
    #     url = base_url.format(x)
    #     parse_page(url)

    for x in range(1,101):
        url = 'https://www.gushiwen.org/default_%s.aspx' % x
        parse_page(url)


if __name__ == '__main__':
    main()
