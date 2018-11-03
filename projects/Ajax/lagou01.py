

import requests
from lxml import etree
import time
import re

# 使用requests抓取拉钩网职位信息

headers = {
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Cookie':'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533889060; _ga=GA1.2.1043657480.1533889060; user_trace_token=20180810161742-da4a9281-9c75-11e8-ba2e-525400f775ce; LGUID=20180810161742-da4a9625-9c75-11e8-ba2e-525400f775ce; JSESSIONID=ABAAABAAAGGABCB0DB926D84FF4B54CD3C05B2C77E05040; index_location_city=%E6%B7%B1%E5%9C%B3; TG-TRACK-CODE=search_code; LGSID=20180910095115-00ab7d79-b49c-11e8-8d12-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F4292395.html; _gat=1; LGRID=20180910100231-938f47e6-b49d-11e8-b62b-5254005c3644; SEARCH_ID=741ec41420a64703b6e477f3a79a6d0c',
        'Host':'www.lagou.com',
        'Origin':'https://www.lagou.com'
    }


def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'

    data = {
        'first':'false',
        'pn':'1',
        'kd':'python'
    }

    for x in range(1, 2):
        data['pn'] = x
        response = requests.post(url, headers=headers, data=data)
        # print(response.json())
        # 如果返回来的是json数据，那么json()方法会直接load成字典
        result = response.json()
        # print(result)
        positions = result['content']['positionResult']['result']
        for position in positions:
            position_id = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html' % position_id
            parse_position_detail(position_url)
            break

        time.sleep(5000)


def parse_position_detail(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    position_name = html.xpath("//span[@class='name']/text()")[0]
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    # . 点号代表当前下面
    salary = job_request_spans[0].xpath('.//text()')[0].strip()
    city = job_request_spans[1].xpath('.//text()')[0].strip()
    city = re.sub(r"[\s/]", "", city)
    work_years = job_request_spans[2].xpath('.//text()')[0].strip()
    work_years = re.sub(r"[\s/]", "", work_years)
    education = job_request_spans[3].xpath('.//text()')[0].strip()
    education = re.sub(r"[\s/]", "", education)
    # "".join 将列表组合成字符串
    desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()

    print(desc)


def main():
    request_list_page()


if __name__ == '__main__':
    main()







