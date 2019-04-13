import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []

def parse_page(url):
    headers = {
        'Referer': 'http://www.weather.com.cn/forecast/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'lxml')
    if url == 'http://www.weather.com.cn/textFC/gat.shtml':
        soup = BeautifulSoup(text, 'html5lib')

    # find()找第一个 find_all查找全部
    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            # 默认取第一个数据，如果是第一行就取第二条
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]

            citys = list(city_td.stripped_strings)[0]
            weather_td = tds[2]
            weathers = list(weather_td.stripped_strings)[0]
            temp_td = tds[-2]
            temps = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'citys':citys,'weathers':weathers,'temps':int(temps)})
            print({'citys':citys,'weathers':weathers,'temps':int(temps)})



def main():
    # url = 'http://www.weather.com.cn/textFC/hb.shtml'
    # url = 'http://www.weather.com.cn/textFC/db.shtml'
    # url = 'http://www.weather.com.cn/textFC/hd.shtml'
    # url = 'http://www.weather.com.cn/textFC/hz.shtml'
    # url = 'http://www.weather.com.cn/textFC/hn.shtml'
    # url = 'http://www.weather.com.cn/textFC/xb.shtml'
    # url = 'http://www.weather.com.cn/textFC/xn.shtml'
    # url = 'http://www.weather.com.cn/textFC/gat.shtml'
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml',
    ]
    for url in urls:
        parse_page(url)

    # 分析数据 根据最低气温排序(可以传递函数)
    # def sorr_key(data):
    #     min_temp = data['']
    #     return min_temp
    ALL_DATA.sort(key=lambda data:data['temps'])
    data = ALL_DATA[0:10]
    # pyecharts 可视化
    # cities = []
    # for city_temp in data:
    #     city = city_temp['city']
    #     cities.append(city)
    cities = list(map(lambda x:x['citys'],data))
    temps = list(map(lambda x:x['temps'],data))
    bar = Bar("标记线和标记点示例")
    bar.add("商家A", cities, temps)
    bar.render('weather.html')



if __name__ == '__main__':
    main()



