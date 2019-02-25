"""
    Created by 朝南而行 2019/2/21 16:55
"""

from lxml import etree
import requests
import time
import json

# 获取中国天气网当天信息


class ChinaWeatherToday(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/68.0.3440.106 Safari/537.36',
            'Referer': 'http://www.weather.com.cn/'
        }

        self.now_time = time.time()
        self.city = input("请输入你想查询的城市：")
        self.url = "http://toy1.weather.com.cn/search?cityname=%s&callback=success_jsonpCallback&_=%.0f" % (self.city, self.now_time)

    def run(self):
        resp = requests.get(url=self.url, headers=self.headers)
        text = resp.text
        # parser = etree.HTMLParser(encoding='utf-8')
        # html = etree.HTML(text, parser=parser)

        content = text.replace('success_jsonpCallback([', '').replace('])', '')


        if len(content) > 0:
            # 只拿匹配到的第一个数据的城市id
            city_id = content.split(',')[0].split('~')[0].split('"')[-1]

            # 10130050119A
            # 101300801019
            # 101300806
            # 101300101
            # 根据id 县 市 区
            # id == 9 为市 区
            # id == 12 为县
            # id == 12 尾号为A 则是景区

            data = []
            if len(city_id) == 9:
                detail_url = 'http://www.weather.com.cn/weather1d/%s.shtml' % city_id
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/68.0.3440.106 Safari/537.36',
                    'Referer': detail_url
                }

                detail_resp = requests.get(url=detail_url, headers=headers)
                # detail_text = detail_resp.text
                detail_text = detail_resp.content.decode('utf-8')
                # print(detail_text)
                parser = etree.HTMLParser(encoding='utf-8')
                html = etree.HTML(detail_text, parser=parser)

                # 通过查找网页中生成的天气预报
                tem = html.xpath("//body//script/text()")[1].split('hour3data=')[-1]
                # 查询到网页的对应的城市
                now_city = "".join(html.xpath("//div[@class='left fl']//div[@class='crumbs fl']/a/text()"))

                print('查询到的城市是：' + now_city + '\n')
                # 转化成Json
                content_weather = json.loads(tem)
                # 1d是今天的相隔几个小时的天气预报
                today_weather_content = content_weather['1d']

                for x in range(0, len(today_weather_content)):
                    # 时间
                    now_time = today_weather_content[x].split(',')[0]
                    # 天气
                    weather = today_weather_content[x].split(',')[2]
                    # 温度
                    temperature = today_weather_content[x].split(',')[3]
                    # 风的吹向
                    wind = today_weather_content[x].split(',')[4]
                    # 风的级数
                    wind_series = today_weather_content[x].split(',')[5]

                    real_time_weather = {
                        'now_time': now_time,
                        'weather': weather,
                        'temperature': temperature,
                        'wind': wind,
                        'wind_series': wind_series
                    }

                    data.append(real_time_weather)

            elif len(city_id) == 12 and city_id[-1] != 'A':
                detail_url = 'http://forecast.weather.com.cn/town/weather1dn/%s.shtml' % city_id
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/68.0.3440.106 Safari/537.36',
                    'Referer': detail_url
                }
                detail_resp = requests.get(url=detail_url, headers=headers)
                # detail_text = detail_resp.text
                detail_text = detail_resp.content.decode('utf-8')
                # print(detail_text)
                parser = etree.HTMLParser(encoding='utf-8')
                html = etree.HTML(detail_text, parser=parser)

                # 查询到网页的对应的城市
                now_city = "".join(html.xpath("//div[contains(@class,'areaSelect')]/a/text()"))

                print('查询到的城市是：' + now_city + '\n')

                content_weather = html.xpath("//div[@class='L_weather']//script/text()")
                # 转化成Json
                today_weather_content = content_weather[0].split('forecast_default')[0].replace('];', '').replace('var', '').replace('forecast_1h = [', '').strip().split('},{')
                # print(json.dumps(today_weather_content, ensure_ascii=False))
                # a = json.loads(today_weather_content)
                # one = today_weather_content.split('},{')

                # print(today_weather_content)
                for x in range(0, len(today_weather_content)):

                    # 时间
                    now_time = today_weather_content[x].split('time":"')[1].split('","weatherCode')[0]
                    # 天气
                    weather = today_weather_content[x].split('weather":"')[1].split('","temp')[0]
                    # 温度
                    temperature = today_weather_content[x].split('temp":')[1].split(',"windL')[0]
                    # 风的吹向
                    wind = today_weather_content[x].split('windD":"')[1].split('"')[0]
                    # 风的级数
                    wind_series = today_weather_content[x].split('windL":"')[1].split('","windD')[0]

                    real_time_weather = {
                        'now_time': str(now_time + '时'),
                        'weather': weather,
                        'temperature': str(temperature + '℃'),
                        'wind': wind,
                        'wind_series': wind_series
                    }

                    data.append(real_time_weather)

            elif len(city_id) == 12 and city_id[-1] == 'A':
                detail_url = 'http://www.weather.com.cn/weather1d/%s.shtml' % city_id
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/68.0.3440.106 Safari/537.36',
                    'Referer': detail_url
                }
                detail_resp = requests.get(url=detail_url, headers=headers)
                # detail_text = detail_resp.text
                detail_text = detail_resp.content.decode('utf-8')
                # print(detail_text)
                parser = etree.HTMLParser(encoding='utf-8')
                html = etree.HTML(detail_text, parser=parser)

                # 通过查找网页中生成的天气预报
                tem = html.xpath("//body//script/text()")[0].split('hour3data=')[-1]
                # 查询到网页的对应的城市
                now_city = "".join(html.xpath("//div[@class='left fl']//div[@class='crumbs fl']/a/text() | //div[@class='left fl']//div[@class='crumbs fl']/span[last()]/text()"))

                print('查询到的城市是：' + now_city + '\n')

                # 转化成Json
                content_weather = json.loads(tem)
                # 1d是今天的相隔几个小时的天气预报
                today_weather_content = content_weather['1d']

                for x in range(0, len(today_weather_content)):
                    # 时间
                    now_time = today_weather_content[x].split(',')[0]
                    # 天气
                    weather = today_weather_content[x].split(',')[2]
                    # 温度
                    temperature = today_weather_content[x].split(',')[3]
                    # 风的吹向
                    wind = today_weather_content[x].split(',')[4]
                    # 风的级数
                    wind_series = today_weather_content[x].split(',')[5]

                    real_time_weather = {
                        'now_time': now_time,
                        'weather': weather,
                        'temperature': temperature,
                        'wind': wind,
                        'wind_series': wind_series
                    }

                    data.append(real_time_weather)

            print(json.dumps(data, ensure_ascii=False))

        else:
            print('没有找到该城市!!!')


if __name__ == '__main__':
    chinaWeather = ChinaWeatherToday()
    chinaWeather.run()
