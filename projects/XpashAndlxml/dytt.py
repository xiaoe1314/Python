from lxml import etree
import requests


# 分页爬取和详情页面
# BASE_URL = 'http://www.ygdy8.com/'
# url = 'http://www.ygdy8.com/html/gndy/dyzz/list_23_1.html'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
# }
#
# resp = requests.get(url=url,headers=headers)
# text = resp.content.decode('gbk')
#
# parser = etree.HTMLParser(encoding='utf-8')
# html = etree.HTML(text,parser=parser)
# detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
# for detail_url in detail_urls:
#     print(BASE_URL+detail_url)

# 1. 先抓取每个页面的详情url
BASE_URL = 'http://www.ygdy8.com/'
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
def get_detail_urls(url):
    resp = requests.get(url=url, headers=HEADERS)
    #text = resp.content.decode('gbk')
    text = resp.text

    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.HTML(text, parser=parser)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    # map将列表的每一项做相同的事情(等价于以下表达式)
    # def abc(url):
    #     return BASE_URL+url
    # index = 0
    # for detail_url in detail_urls:
    #     detail_url = abs(detail_url)
    #     detail_urls[index] = detail_url
    #     index += 1
    detail_urls = map(lambda url:BASE_URL+url,detail_urls)
    return detail_urls

def parse_detail_page(url):
    movies = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font/text()")[0]
    movies['title'] = title
    imgs = html.xpath("//div[@id='Zoom']//img")

    if len(imgs) > 0:
        if len(imgs) == 1:
            cover = imgs[0]
            movies['cover'] = cover
            screenshot = ''
            movies['screenshot'] = screenshot
        if len(imgs) == 2:
            cover = imgs[0]
            movies['cover'] = cover
            screenshot = imgs[1]
            movies['screenshot'] = screenshot

    infos = html.xpath("//div[@id='Zoom']//text()")

    actors = []
    abstracts = []

    # for info in infos:
    for index,info in enumerate(infos):
        # print(info)
        # print(index)
        # startswith 函数是判断前面字符是否一样
        if info.startswith('◎年　　代'):
            #replace 是替换函数  strip 将一个字符串的前后空字符全部删掉
            year = info.replace('◎年　　代','').strip()
            movies['year'] = year

        elif info.startswith('◎产　　地'):
            # replace 是替换函数  strip 将一个字符串的前后空字符全部删掉
            country = info.replace('◎产　　地', '').strip()
            movies['country'] = country

        elif info.startswith('◎类　　别'):
            # replace 是替换函数  strip 将一个字符串的前后空字符全部删掉
            category = info.replace('◎类　　别', '').strip()
            movies['category'] = category

        elif info.startswith('◎语　　言'):
            # replace 是替换函数  strip 将一个字符串的前后空字符全部删掉
            language = info.replace('◎语　　言', '').strip()
            movies['language'] = language

        elif info.startswith('◎主　　演'):
            # replace 是替换函数  strip 将一个字符串的前后空字符全部删掉
            actor = info.replace('◎主　　演', '').strip()
            actors = [actor]
            for x in range(index+1,len(infos)):
                if infos[x].startswith('◎简　　介 '):
                    break
                actors.append(infos[x].strip())
            movies['actors'] = actors

        elif info.startswith('◎简　　介'):
            # replace 是替换函数  strip 将一个字符串的前后空字符全部删掉
            # abstract = info.replace('◎简　　介', '').strip()
            for x in range(index + 1, len(infos)):
                if infos[x].startswith('【下载地址】'):
                    break
                abstract = infos[x].strip()
                abstracts.append(abstract)
            movies['abstract'] = abstracts

    download_url = html.xpath("//div[@id='Zoom']//td[@style='WORD-WRAP: break-word']/a/@href")[0]
    movies['download_url'] = download_url
    return movies


def spider():
    base_url = 'http://www.ygdy8.com/html/gndy/dyzz/list_23_{}.html'
    for x in range(1,8):
        url = base_url.format(x)
        movie_detail_urls = get_detail_urls(url)
        for movie_detail_url in movie_detail_urls:
            movies = parse_detail_page(movie_detail_url)
            print(movies)


if __name__ == '__main__':
    spider()







