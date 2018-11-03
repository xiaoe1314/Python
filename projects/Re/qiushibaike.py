import requests
import re
import json

# 正则表达式实战抓取糗事百科网页


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    text = response.text
    # <div\sclass="cont"> 某个div下面
    # .* 多个任意字符  . 点号不能匹配到 \n 在后面加 re.DOTALL 可以让 . 点号匹配所有字符
    # 匹配个字符需要非贪婪模式 加 ?


    imgs = re.findall(r'<div\sclass="author\sclearfix">.*?<img src="(.*?)".*?>', text, re.DOTALL)
    author_tags = re.findall(r'<div\sclass="author\sclearfix">.*?<h2>(.*?)</h2>', text, re.DOTALL)
    authors = []
    for author in author_tags:
        authors.append(author.strip())

    articleGenders = re.findall(r'div\sclass="author\sclearfix">.*?<div\sclass="articleGender\s.*?">(.*?)</div>', text, re.DOTALL)

    content_tags = re.findall(r'<div\sclass="content">.*?<span>(.*?)</span>',text,re.DOTALL)
    contents = []
    for content in content_tags:
        x = re.sub('<.*?>','',content)
        contents.append(x.strip())

    statsVotes = re.findall(r'<div\sclass="stats">.*?<span\sclass="stats-vote">.*?<i\sclass="number">(.*?)</i>', text, re.DOTALL)
    statsComments = re.findall(r'<div\sclass="stats">.*?<span\sclass="stats-comments">.*?<i\sclass="number">(.*?)</i>', text, re.DOTALL)


    peoms = []
    for value in zip(imgs,authors,articleGenders,contents,statsVotes,statsComments):
        img,author,articleGender,content,statsVote,statsComment = value
        peom = {
            'img':img,
            'author':author,
            'articleGender':int(articleGender),
            'content':content,
            'statsVote':int(statsVote),
            'statsComment':int(statsComment)
        }
        peoms.append(peom)

    print("="*200)
    print(peoms)
    print("=" * 200)
    json_peoms = json.dumps(peoms,ensure_ascii=False)
    with open('qsbk.json', 'w', encoding='utf-8') as fp:
        fp.write(json_peoms)
    print("=" * 200)
    print(json_peoms)
    print("=" * 200)

    # ensure_ascii=False 解码 Unicode
    # with open('qsbk.json','w',encoding='utf-8') as fp:
        # 转换为文件
        # json.dump(peoms,fp,ensure_ascii=False)

    # 将python对象转换成json字符串
    # json.dump  json.dumps
    # 将json字符串转换成python对象
    # json.load  json.loads


def main():
    # base_url = 'https://www.qiushibaike.com/8hr/page/{}/'
    # for x in range(1,14):
    #     url = base_url.format(x)
    #     parse_page(url)

    for x in range(1,14):
        url = 'https://www.qiushibaike.com/8hr/page/%s/' % x
        parse_page(url)


if __name__ == '__main__':
    main()
