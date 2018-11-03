# -*- coding: utf-8 -*-
# 1、获取所有的城市url链接
# 	http://www.fang.com/SoufunFamily.htm
#
# 2、获取所有城市新房的链接
#
# 	例如：南宁：http://nn.fang.com/
# 	南宁新房：http://nn.newhouse.fang.com/house/s/
#
# 3、获取所有城市二手房的链接
#
# 	例如：南宁：http://nn.fang.com/
# 	南宁二手房：http://nn.esf.fang.com/
#
#
# 4、北京是个例外：
#
# 	北京城市url:http://bj.fang.com/
# 	北京的新房url：http://newhouse.fang.com/house/s/
# 	北京的二手房url:http://esf.fang.com/
import scrapy
import re
from fang.items import NewHouseItem, EsfItem
# 第一步
from scrapy_redis.spiders import RedisSpider


class SfwSpider(RedisSpider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    # 第二步
    # start_urls = ['http://www.fang.com/SoufunFamily.htm']
    redis_key = "fang:start_urls"

    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            # 找没有class的属性的td标签
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0]
            province_text = province_td.xpath(".//text()").get()
            province_text = re.sub(r"\s", "", province_text)
            # 保存省份(如果查找省份为空白字符，则和上一个省份一样)
            if province_text:
                province = province_text
            # 不爬取海外城市的房源信息
            if province == "其它":
                continue
            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # print("省份：" + province)
                # print("城市：" + city)
                # print("城市url：" + city_url)

                url_module = city_url.split("//")
                scheme = url_module[0]
                domain = url_module[1]
                domain_module = domain.split(".")
                domain_module1 = domain_module[0]
                # domain_module2 = domain_module[1]
                # domain_module3 = domain_module[2]
                # print('==='+domain_module1+'===')
                if domain_module1 == "bj":
                    new_house_url = 'http://newhouse.fang.com/house/s/'
                    esf_url = 'http://esf.fang.com'
                else:
                    # 新房链接
                    new_house_url = scheme + "//" + domain_module1 + ".newhouse.fang.com/house/s/"
                    # 二手房链接
                    esf_url = scheme + "//" + domain_module1 + ".esf.fang.com"

                yield scrapy.Request(url=new_house_url, callback=self.parse_newhouse, meta={"info": (province, city)})
                yield scrapy.Request(url=esf_url, callback=self.parse_esf, meta={"info": (province, city)})

    def parse_newhouse(self, response):
        province, city = response.meta.get('info')
        # contains  div里面的class属性包含有nl_con属性
        lis = response.xpath("//div[contains(@class,'nl_con')]//ul//li")
        for li in lis:
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get()
            if name:
                name = name.strip()
                # print(name)
            price1 = li.xpath(".//div[@class='nhouse_price']/span/text()").get()
            price2 = li.xpath(".//div[@class='nhouse_price']/em/text()").get()
            price = str(price1) + str(price2)
            if price:
                price = price.strip()
                # print(price)
            rooms = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
            if rooms:
                rooms = "".join(rooms).strip()
                # print(rooms)
            area = li.xpath(".//div[contains(@class,'house_type')]/text()").getall()
            if area:
                area = "".join(area).strip()
                area = re.sub(r'\s|/|－', '', area)
                # print(area)
            address = li.xpath(".//div[contains(@class,'address')]/a/text()").getall()
            if address:
                address = "".join(address).strip()
                address = re.sub(r'\s', '', address)
                # print(address)
            district = li.xpath(".//div[contains(@class,'address')]/a/span/text()").get()
            if district:
                district = re.sub(r'\s|\[|\]', '', district)
                # print(district)
            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
            if sale:
                sale = sale.strip()
                # print(sale)
            origin_url = li.xpath(".//div[contains(@class,'nlcd_name')]/a/@href").get()
            if origin_url:
                origin_url = origin_url.strip()
                # print(origin_url)

            if name:
                yield NewHouseItem(
                    province=province,
                    city=city,
                    name=name,
                    price=price,
                    rooms=rooms,
                    area=area,
                    address=address,
                    district=district,
                    sale=sale,
                    origin_url=origin_url
                )
            else:
                continue
        next_url = response.xpath("//div[@class='page']//a[contains(@class,'next')]/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse, meta={"info": (province, city)})

    def parse_esf(self, response):
        province, city = response.meta.get('info')
        lis = response.xpath("//div[contains(@class,'shop_list')]/dl")
        for li in lis:
            name = li.xpath(".//dd/h4[@class='clearfix']/a/span/text()").get()
            if name:
                name = name.strip()

            info = li.xpath(".//dd/p[@class='tel_shop']/text()").getall()
            rooms = None
            area = None
            floor = None
            toward = None
            year = None
            if info:
                if len(info) >= 1 and info[0]:
                    rooms = re.sub(r'\s', '', info[0])

                if len(info) >= 2 and info[1]:
                    area = re.sub(r'\s', '', info[1])

                if len(info) >= 3 and info[2]:
                    floor = re.sub(r'\s', '', info[2])

                if len(info) >= 4 and info[3]:
                    toward = re.sub(r'\s', '', info[3])

                if len(info) >= 5 and info[4]:
                    year = re.sub(r'\s', '', info[4])

            address_info1 = li.xpath(".//dd/p[@class='add_shop']/a/text()").get()
            address_info2 = li.xpath(".//dd/p[@class='add_shop']/span/text()").get()
            address = str(address_info1) + str(address_info2)
            if address:
                address = re.sub(r'\s', '', address)

            price1 = li.xpath(".//dd[@class='price_right']/span/b/text()").get()
            price2 = li.xpath(".//dd[@class='price_right']/span/text()").get()
            price = str(price1) + str(price2)
            if price:
                price = price.strip()

            unit = li.xpath(".//dd[@class='price_right']/span[2]/text()").get()
            if unit:
                unit = unit.strip()

            origin_url = li.xpath(".//dd/h4[@class='clearfix']/a/@href").get()
            if origin_url:
                # origin_url = response.url + origin_url.lstrip('/')
                origin_url = response.urljoin(origin_url)

            yield EsfItem(
                province=province,
                city=city,
                name=name,
                rooms=rooms,
                area=area,
                floor=floor,
                toward=toward,
                year=year,
                address=address,
                price=price,
                unit=unit,
                origin_url=origin_url
            )

        texts = response.xpath("//div[@class='page_al']/p/a/text()").getall()
        urls = response.xpath("//div[@class='page_al']/p/a/@href").getall()
        # 取倒数第二个的url，如果倒数第二个是下一页的文本着进行下一页的操作
        next_url = urls[len(urls)-2]
        if texts[len(texts) - 2] == '下一页':
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_esf, meta={"info": (province, city)})












