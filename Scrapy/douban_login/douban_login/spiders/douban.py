# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from PIL import Image


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']
    login_url = 'https://accounts.douban.com/login'
    profile_url = 'https://www.douban.com/people/164125969/'

    def parse(self, response):
        formdata = {
            'source': 'None',
            'redir': 'https://www.douban.com/',
            'form_email': '15907813604',
            'form_password': 'xiaoe520',
            'login': '登录'
        }

        captcha_url = response.css("img#captcha_image::attr(src)").get()
        # captcha_url = response.xpath("//img[@id='captcha_image']/@src").get()

        print('*' * 50)
        print(captcha_url)
        print('*' * 50)

        if captcha_url:
            captcha = self.regonize_captcha(captcha_url)
            formdata['captcha-solution'] = captcha
            captcha_id = response.xpath("//input[@name='captcha-id']/@value").get()
            formdata['captcha-id'] = captcha_id
        yield scrapy.FormRequest(url=self.login_url, formdata=formdata, callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.url == 'https://www.douban.com/':
            print('登录成功')
            yield scrapy.FormRequest(url=self.profile_url, callback=self.parse_profile)
        else:
            print('登录失败')

    def parse_profile(self, response):
        if response.url == self.profile_url:
            print('进入到了个人中心' + response.url)
            changeName = input('请输入要修改的昵称？')
            ck = response.xpath("//input[@name='ck']/@value").get()
            formdata = {
                'ck': ck,
                'signature': changeName
            }
            yield scrapy.FormRequest('https://www.douban.com/j/people/164125969/edit_signature', formdata=formdata)

        else:
            print('进入失败：' + response.url)

    def regonize_captcha(self, image_url):
        request.urlretrieve(image_url, 'captcha.png')
        image = Image.open('captcha.png')
        image.show()
        captcha = input('请输入验证码:')
        return captcha


















