"""
    Created by 朝南而行 2018/12/31 9:39
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
from lxml import etree


class Reply(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\Python\chromedriver.exe')
        self.url = 'https://tieba.baidu.com'
        self.login_url = 'https://tieba.baidu.com/index.html'
        self.school_url = 'http://tieba.baidu.com/f/index/forumpark?pcn=%E7%94%B5%E5%BD%B1&pci=0&ct=1&rn=20&pn=1'
        # self.school_url = 'http://tieba.baidu.com/f/index/forumpark?pcn=%E6%B8%B8%E6%88%8F&pci=0&ct=1&rn=20&pn=1'
        # self.school_url = 'http://tieba.baidu.com/f/index/forumpark?pcn=%E9%AB%98%E7%AD%89%E9%99%A2%E6%A0%A1&pci=0&ct=1&rn=20&pn=1'
        self.test_url = 'http://tieba.baidu.com/f?kw=985'
        self.num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.test_main = [
            '`=== `每`天`@更`新`hongbao`活`动``wx`guan`住` `小黑`线`报`===`',
            '`===`wx`guan`住` `小黑`线`报``@教`你`开通`zhi`fu`bao`免`费`提`现`和`提`现`秒`到`yin`行`卡===`',
            '`=== `wx`guan`住` `小黑`线`报`@兼职``####@@@曰`赚`100`===`',
            '`=== `wx`guan`住` `小黑`线`报``@免`费`看`VIP`电`影`请`===`',
            '`===`wx`guan`住` `小黑`线`报``@ling``VIP`看`电`影@`===`'
        ]
        self.text_list = [
            '你离死亡最近的一次经历？神回复：二十年前，差点给后面那精子追上了！',
            '为什么我们会围在一起讨论高考作文，而不是数学或物理？网友：因为，这是我们现在唯一还看得懂的东西。',
            '为什么中国领导访问日本，日本方面比较冷淡，甚至机场连欢迎标语都没挂？神回复：怎么挂？热烈欢迎老朋友来日？',
            '八戒说：师兄，你快去医院看看，医院专门为你开了一个科室！悟空：哦，什么科室？八戒：二逼猴科！',
            '有一个女玩家在论坛上发贴问：“光棍节想向心仪的男生表白，送点什么礼物好？”神回复：First Blood。',
            '发现男朋友有个微博小号，关注了前女友和若干公司的美女，怎么办？神回复：分了吧，这男人的智商让人捉急，这都能被发现！',
            '记者又问：“你认为爱国主义的表现是什么？”神回复：移民，给资本主义添乱。',
            '刚刚看到有人说中国平均工资是4134元钱！神回复：平均工资能说明什么问题？潘长江和姚明平均身高是196CM，能说明什么？潘长江很高吗？',
            '都40多了，还有许多事不明白该问谁？神回复：外事问谷歌，内事问百度，房事问天涯！',
            '以前有一朋友在空间里发表了一句说说：“给我一个姑娘，我能创造一个民族！”神评论：“给你一头母猪，你能不能创造一个新品种！',
            '公交车上看见一个合口味的男生，怎么勾搭？神回复：假装癫痫，口吐白沬，倒他怀里，双手抽搐，趁机抓他裆，够大就继续，不满意就——哎！我好了！',
            '今天看到同学空间秀儿子刚出生的照片。看到一条评论亮瞎了我的眼。神回复：看到你儿子长的一点都不像我。那我就放心了。',
            '都40多了，还有许多事不明白该问谁？神回复：外事问谷歌，内事问百度，房事问天涯！',
            'CCTV又采访了，记者问 作为一个中国人你能为祖国做些什么？神回复：“移民，不给祖国添乱。',
            '女朋友赌气关机，怎么办？神回复：楼主去理发吧，方便戴帽子。',
            '老婆是路，朋友是牛，人生只有一条路，路上会有好多牛，有钱时别走错路，没钱时别卖牛！神回复：牛上路了咋办？',
            '为什么CCTV新闻放完以后，总要播出他们在收拾稿子的片段？神回复：为了告诉你，我们吹牛是打草稿的！',
            '别人的孩子都会买手纸了，我的孩子还在手纸上。神回复：别人的老婆都会生气了，你的老婆还要充气。',
            '听到一特好听的歌，歌词只记得是“一个芝麻糕，不如一针细”，求歌名啊！神回复：你可知Macau，不是我真姓。',
            '男朋友第一次见岳父岳母，送些什么好呢？神回复：外孙或外孙女儿。',
            '当时的理科二本线450，三本线400，也就是说如果不努点力330连三本都没得上了',
            '高一耍得太嗨了，单词没怎么背过 现在从头开始背，但是背了又忘背了又忘',
            '你这样多打击吧里某些人，他们也说自己读不懂，但是他们才三四十分四五十分',
            '多吃点核桃？？？我英语全是因为美剧，不知道你有没有时间看。需要的话我可以整理点方法吧，你真看我就整理',
            '拿11题来说第一个是常规方法，但是运算量大的死人，第二个是简易方法（当时没学参数），注释中是我的独特方法（纯属瞎掰搞出来）',
            '高考成绩镇楼，看到了很多帖子问数学怎么提高，我也懒得说无数次，直接发帖帮助他们吧。这个帖子专门解决数学方面的学习问题。',
            '一直感觉错题本没有什么用，需要记录的使用是好的思路，好的方法的题目，就是自己感觉很好的题目； 在形式上错题本感觉意义不大',
            '没怎么看懂你的意思，不过我只是提建议，你们随意，不喜欢就不做，认为有问题我们可以讨论是吧',
            '我也觉得错题没什么用，纯粹浪费时间 情愿多看几遍卷子',
            'IG夺冠，就这点表示!!!!!打发谁呢,老哥们，都去发微博啊，顶上热搜',
            '这样没用的，他回头给你搞点什么活动，玩家一买皮肤什么的，销量一上来，根本不会炒这种策划的，',
        ]

    def run(self):
        self.login()
        self.all_school()

    def login(self):
        self.driver.get(self.login_url)
        print('正在等待登录中...')
        # 等待 登录
        WebDriverWait(driver=self.driver, timeout=1000).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='u_username_title']"))
        )
        print('登录成功')
        time.sleep(2)

    def all_school(self):
        # 打开高校的窗口
        self.driver.execute_script("window.open('%s')" % self.school_url)
        # 切换到首页的窗口
        self.driver.switch_to_window(self.driver.window_handles[0])
        # 关闭首页的窗口
        self.driver.close()
        # 切换到高校的窗口
        self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles) - 1])
        time.sleep(2)
        print('开始进入所有高校页===' + self.school_url)
        while True:
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            # page_source这个方法可以拿到全部代码包括ajax返回来的
            source = self.driver.page_source
            self.parse_list_page(source)
            # 等待
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='pagination']//a[@class='next']"))
            )
            next_btn = self.driver.find_element_by_xpath("//div[@class='pagination']//a[@class='next']")
            # get_attribute获取属性
            if 'next' in next_btn.get_attribute("class"):
                next_btn.click()
            else:
                pass
            time.sleep(2)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//div[contains(@class,'ba_list')]/div[contains(@class,'ba_info')]/a/@href")
        print('成功获取所有的高校贴吧详情页' + str(links))
        for link in links:
            try:
                self.request_detail_page(self.url + link)
            except:
                continue

    def request_detail_page(self, url):
        time.sleep(2)
        print('成功打开高校贴吧详情页===' + url)
        # 打开详情的窗口
        self.driver.execute_script("window.open('%s')" % url)
        # 切换到详情的窗口
        self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles) - 1])
        source = self.driver.page_source

        self.parse_detail_page(source)

        # 关闭详情的窗口
        self.driver.close()
        # 切换到列表页
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        time.sleep(2)
        html = etree.HTML(source)
        name_list = html.xpath("//div[contains(@class,'card_title')]//a/text()")
        name = "".join(name_list).strip()

        # 等待 关注 按钮
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='focus_btn_wrap']"))
        )
        follow_btn = self.driver.find_element_by_xpath("//div[@class='focus_btn_wrap']")
        follow_btn.click()
        time.sleep(2)

        # 等待 关闭关注窗口 按钮
        try:
            follow_btn = self.driver.find_element_by_xpath("//div[@class='dialogJtitle']/a")
            follow_btn.click()
            print('成功关注了===' + str(name))
        except:
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='dialogJbody']/a[last()]"))
            )
            cancel_btn = self.driver.find_element_by_xpath("//div[@class='dialogJbody']/a[last()]")
            cancel_btn.click()
            print('您已经关注过了' + str(name))
        time.sleep(2)

        # 等待 签到 按钮
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='signstar_wrapper']/a"))
        )
        sign_on_btn = self.driver.find_element_by_xpath("//div[@id='signstar_wrapper']/a")
        print("title属性===" + str(sign_on_btn.get_attribute("title")))
        if str(sign_on_btn.get_attribute("title")) == '签到':
            sign_on_btn.click()
            print(str(name) + '===签到成功')
        else:
            print('今日您已签到，无需在签到')
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(3)

        num = random.choice(self.num)
        print(num)
        if num == 8:
        # 输入内容与回复
            source2 = self.driver.page_source
            html2 = etree.HTML(source2)
            detail_urls = html2.xpath(
                "//div[contains(@id, 'pagelet_frs-list/pagelet/thread_list')]/ul/li//div[contains(@class, 'threadlist_title pull_left j_th_tit')]/a/@href")[
                          2:3]
            print(str(detail_urls))
            for detail_url in detail_urls:
                detail_url = self.url + detail_url
                print(str(detail_url))
                self.request_detail_hui_page(detail_url)
                time.sleep(8)

    def request_detail_hui_page(self, url):
        print('成功打开回复详情页===' + url)
        # 打开详情的窗口
        self.driver.execute_script("window.open('%s')" % url)
        # 切换到详情的窗口
        self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles) - 1])
        time.sleep(3)
        print('开始滑动')
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        source = self.driver.page_source
        html = etree.HTML(source)
        hui_nexts = html.xpath(
            "//div[contains(@class,'p_postlist')]//div[contains(@class,'core_reply_tail')]//a[@class='lzl_link_unfold']/text()")
        print(len(hui_nexts))
        for hui_next in hui_nexts:

            try:
                # 等待 回复 按钮
                WebDriverWait(driver=self.driver, timeout=10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[contains(@class,'p_postlist')]//div[contains(@class,'core_reply_tail')]//a[@class='lzl_link_unfold']"))
                )
                follow_btn = self.driver.find_element_by_xpath(
                    "//div[contains(@class,'p_postlist')]//div[contains(@class,'core_reply_tail')]//a[@class='lzl_link_unfold']")

                if str(hui_next) == '回复':
                    follow_btn.click()
                else:
                    # 等待 回复下一级 按钮
                    WebDriverWait(driver=self.driver, timeout=10).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        "//div[contains(@class,'p_postlist')]//div[contains(@class,'j_lzl_container')]/div/ul/li//a[@class='lzl_s_r']"))
                    )
                    follow_btn_other = self.driver.find_element_by_xpath(
                        "//div[contains(@class,'p_postlist')]//div[contains(@class,'j_lzl_container')]/div/ul/li//a[@class='lzl_s_r']")
                    follow_btn_other.click()

                time.sleep(2)
                # 等待 输入框 按钮
                WebDriverWait(driver=self.driver, timeout=10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[contains(@class,'p_postlist')]//div[contains(@class,'j_lzl_container')]//div[contains(@class,'editor_for_container')]"))
                )
                follow_input = self.driver.find_element_by_xpath(
                    "//div[contains(@class,'p_postlist')]//div[contains(@class,'j_lzl_container')]//div[contains(@class,'editor_for_container')]")
                text_start = random.choice(self.text_list)[0:random.randint(5, 20)]
                text_end = random.choice(self.text_list)[random.randint(15, 20):-1]
                text = text_start + random.choice(self.test_main) + text_end
                follow_input.send_keys(text)
                print('输入成功' + text)
                time.sleep(2)

                # 等待 发表 按钮
                WebDriverWait(driver=self.driver, timeout=10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[contains(@class,'p_postlist')]//div[contains(@class,'j_lzl_container')]//table[contains(@class,'lzl_panel_wrapper')]//div[@class='lzl_panel_btn']/span[1]"))
                )
                follow_input_up = self.driver.find_element_by_xpath(
                    "//div[contains(@class,'p_postlist')]//div[contains(@class,'j_lzl_container')]//table[contains(@class,'lzl_panel_wrapper')]//div[@class='lzl_panel_btn']/span[1]")
                follow_input_up.click()
                print('发布成功' + text)
                time.sleep(2)
            except:
                continue

        # 关闭详情的窗口
        self.driver.close()
        # 切换到列表页
        self.driver.switch_to_window(self.driver.window_handles[1])


if __name__ == '__main__':
    spider = Reply()
    spider.run()


