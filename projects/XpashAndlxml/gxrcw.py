from lxml import etree
import requests


# 实战抓取广西人才网最新的python工程师的招聘信息

BASE_URL = 'http://s.gxrc.com/'
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


def spider():
    base_url = 'http://s.gxrc.com/sJob?schType=1&pageSize=20&orderType=0&listValue=1&keyword=python&page={}'
    for x in range(1,7):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            detail = parse_detail_page(detail_url)
            print(detail)


def parse_detail_page(url):
    detail = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    # lxml + xpath
    html = etree.HTML(text)
    job = html.xpath("//div[@class='gsR_con']//h1[@id='positionName']/text()")[0]
    detail['job'] = job.strip()
    company = html.xpath("//div[@class='gsR_con']//a/text()")[0]
    detail['job'] = company

    infos = html.xpath("//div[@class='gsR_con']/table[@class='gs_zp_table']//td/text()")

    for index,info in enumerate(infos):
        if index == 0:
            detail['num'] = info.strip()
        elif index == 1:
            detail['education'] = info.strip()
        elif index == 2:
            detail['wages'] = info.strip()
        elif index == len(infos)-1:
            detail['welfare'] = info.strip()

    jobContentList = []
    jobContents = html.xpath("//div[@class='gz_info_txt']//p/text()")
    for jobContent in jobContents:
        jobContentList.append(jobContent.strip())
        print(jobContent)

    detail['jobContentList'] = jobContentList

    # num = html.xpath("//div[@class='gs_zp_table']//a/text()")[0]
    # detail['num'] = num
    # education = html.xpath("//div[@class='gs_zp_table']//a/text()")[0]
    # detail['education'] = education
    # wages = html.xpath("//div[@class='gsR_con']//a/text()")[0]
    # detail['wages'] = wages
    # welfare = html.xpath("//div[@class='gsR_con']//a/text()")[0]
    # detail['welfare'] = welfare
    # print(company)

    return detail


def get_detail_urls(url):
    resp = requests.get(url=url, headers=HEADERS)
    text = resp.content.decode('utf-8')

    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.HTML(text, parser=parser)
    detail_urls = html.xpath("//div[@class='rlOne']//li[@class='w1']//a/@href")
    # map将列表的每一项做相同的事情(等价于以下表达式)
    # def abc(url):
    #     return BASE_URL+url
    # index = 0
    # for detail_url in detail_urls:
    #     detail_url = abs(detail_url)
    #     detail_urls[index] = detail_url
    #     index += 1
    #detail_urls = map(lambda url:BASE_URL+url,detail_urls)
    return detail_urls


if __name__ == '__main__':
    spider()






