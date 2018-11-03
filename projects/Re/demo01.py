import re


# 匹配某个字符串

# text = 'hello'
# match函数只能从开始匹配
# ret = re.match('he',text)
# search函数可以全局匹配
# ret = re.search('ll',text)
# print(ret.group())

# 2 点（.）匹配任意字符

# 3 \d匹配任意数字

# 4 \D匹配任意的非数字

# 5 \s匹配的是空白字符（\n,\t,\r,空格）
# text = ' '
# ret = re.match('\s',text)
# print(ret.group())

# 6 \w匹配的是a-z,A-Z 已经数字和下划线

# 7 \W 匹配到小写W(\w)匹配不到的

# 8 []组合的方式，只要满足中括号的字符就可以匹配
# 匹配多个字符 在后面添加一个  +
# text = '0771-8888888'
# ret = re.match('[\d\-]+',text)
# print(ret.group())

# 8.1 中括号的方式代替/d
# text = '0771-8888888'
# ret = re.match('[0-9]',text)
# print(ret.group())

# 8.2 中括号的方式代替/D(托字号)
# text = '0771-8888888'
# ret = re.match('[^0-9]',text)
# print(ret.group())

# 8.3 中括号的方式代替/w
# text = 'a'
# ret = re.match('[a-zA-Z0-9_]',text)
# print(ret.group())


# 8.4 中括号的方式代替/W
# text = '#'
# ret = re.match('[^a-zA-Z0-9_]',text)
# print(ret.group())


# 9 * 星号匹配0或多个字符
# text = '0771-8888888'
# ret = re.match('\d*',text)
# print(ret.group())


# 10 + 加号匹配1或多个字符（最少一个）
# text = '0771-8888888'
# ret = re.match('\w+',text)
# print(ret.group())

# 11 ? 问号匹配一个或者零个（最多一个）
# text = '0771-8888888'
# ret = re.match('\w?',text)
# print(ret.group())


# 12 {1} 匹配m个字符
# text = "abcd"
# ret = re.match('\w{4}',text)
# print(ret.group())

# 13 {n,m} 匹配n到m个字符
# text = '123456'
# ret = re.match('\w{1,8}',text)
# print(ret.group())


# 14 实战匹配手机号码
# text = '13907813604'
# ret = re.match('1[34578]\d{9}',text)
# print(ret.group())


# 15 实战匹配邮箱(使用\进行转义)
# text = '19457558dd@163.com'
# ret = re.match('\w+@[a-z0-9]+\.[a-z]+',text)
# print(ret.group())


# 16 实战匹配url
# text = 'http://www.baidu.com.cn'
# ret = re.match('(http|https|ftp)://[^\s]+',text)
# print(ret.group())


# 17 实战匹配身份证
# text = '450802199604021234'
# print(len(text))
# ret = re.match('\d{17}[\dxX]|\d{14}[\dxX]',text)
# print(ret.group())


# 18 ^（脱字号） 代表以什么开始或者取反
# text = 'hello'
# ret = re.match('^o',text)
# print(ret.group())


# 19 $ 表示以什么什么结尾
# text = 'fafa@163.com'
# ret = re.match('\w+@163.com$',text)
# print(ret.group())

# 20 | 并集的操作（匹配多个字符串或者表达式）
# text = 'fafa@163.com'
# ret = re.match('\w+@163.com$',text)
# print(ret.group())

# 21 贪婪模式和非贪婪模式 +贪婪模式 +?非贪婪模式
# text = '<h1>标题</h1>'
# ret = re.match('<.+?>',text)
# print(ret.group())


# 22 实战匹配0到100之家的数字
# 可以出现 1 3 4 10 不可以出现 09 101
# 三种情况 0 1 99 100
# text = '90'
# ret = re.match('0$|[1-9]\d?$|100$',text)
# print(ret.group())


# 23 匹配原生字符串要用转义字符 \ 和实战匹配价格
# text = 'apple price is $299'
# ret = re.search('\$\d+',text)
# print(ret.group())

# 24 原生字符（去掉原生意思有两种方法）
# 1. 共同方法加 \  2.python语法前面加  r  （r - raw - 原生的）
# text = '\\n'
# text = r'\n'
# print(text)


# text = '\\n'
# ret = re.match('\\\\n',text)
# print(ret.group())


# 25 group分组
# text = 'apple price is $299,orange price is $10'
# ret = re.search('.*(\$\d+).*(\$\d+)',text)
# print(ret.group())
# print(ret.group(0))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(1,2))
# 所有的子分组都拿出来
# print(ret.groups())


# 26 findall函数(返回一个列表)
# text = 'apple price is $299,orange price is $10'
# ret = re.findall('\$\d+',text)
# print(ret)


# 27 sub函数（替换函数）
# 参数 1正则  2替换成啥  3在哪里替换  4替换多少个
# text = 'apple price is $299,orange price is $10'
# ret = re.sub('\$\d+','0',text,2)
# print(ret)


# 28 sub函数实战获取拉勾网职位信息

# html = """
# <div>
# <p>岗位职责：</p>
# <p>1、负责公司量化交易平台的设计和开发维护</p>
# <p>2、平衡需求复杂度和技术可行性，参与项目需求评估和优化设计</p>
# <p>3、协助技术负责人提高团队的代码质量和工作效率，营造技术氛围</p>
# <p><br></p>
# <p>岗位优势：</p>
# <p>1、量化策略团队实力雄厚，由知名985高校的<strong>博士</strong>、<strong>硕</strong>士组成的年轻而有活力的团队，部分成员来自<strong>百亿级</strong>私募，有丰富的大资金操作经验，能够大大拓客业务视野，更好地实现技术变现；</p>
# <p>2、团队扁平，推崇<strong>创业</strong>、<strong>共赢</strong>的理念，邀请优秀的你加入我们，一起变得更好。</p>
# <p><br></p>
# <p>&nbsp;</p>
# <p>职位要求:</p>
# <p>1、3年以上Python经验，熟悉Django, Tornado, Flask框架中的至少一种，熟悉Web后端架构</p>
# <p>2、熟悉Linux平台环境的开发，掌握Linux常用命令</p>
# <p>3、熟悉python网络编程，能够设计和维护基于TCP/IP协议的高性能事件驱动框架程序</p>
# <p>4、熟悉mysql、mongodb、redis等数据库使用</p>
# <p>5、掌握基于WebSoceket的单页应用的开发思想和技术栈</p>
# <p>&nbsp;</p>
# <p>有下列经验的加分</p>
# <p>1、有zeromq或者其他RPC框架的实际项目经验加分</p>
# <p>2、有<strong>Docker Swarm</strong>、<strong>K8S</strong>等项目实际经验优先</p>
# <p>3、有大型分布式websocket项目经验优先</p>
# <p><br></p>
# <p>我们将为您提供：</p>
# <p>0、终身快速科学上网服务（全球各地有SS节点），<strong>机房专线</strong>直达办公室</p>
# <p>1、薪资：我们提供行业内有竞争力的薪酬；（BTW: 试用期是 <strong>100%</strong>薪资）</p>
# <p>2、奖金+提成：优秀的您可以共享公司的经营业绩，直接每月兑现公司总销售利润；</p>
# <p>3、基本保障福利：公司按照国家规定为员工实额缴纳社会保险；</p>
# <p>4、额外补充福利：</p>
# <p>* 晋升加薪类：每年有超过行业平均的加薪幅度；</p>
# <p>* 礼金礼品类: 过节费、各类礼金等；</p>
# <p>* 员工关怀类: “家人生日会“(程序猿/媛的生日可以更加丰富多彩的）</p>
# <p>* 团队建设类：团队月度“腐败”活动+“每天充足的零食”+<strong>设备补贴</strong>（以补贴一个15寸高配rMBP的价格来每月返还）</p>
# <p>* 年度旅游+自由度大+提升空间大+快速成长期，等等!来了你就知道！</p>
# <p><br></p>
# <p>注意，团队马上进驻天河区<strong>珠江新城富力盈丰</strong>大厦，目前面试地点在<strong>番禺节能科技园总部中心2号楼1903</strong>。</p>
#         </div>
# """

# 默认贪婪模式
# ret = re.sub('<.+>','',html)
# 加 ? 为非贪婪模式
# ret = re.sub('<.+?>',"",html)
# print(ret)


# 29 split函数
# text = 'hello&world ni hao'
# ret = re.split(' ',text)
# ret = re.split('[^a-zA-Z]',text)
# print(ret)

# 30 compile用于提高编译速度
text = 'the number is 20.50'
# r = re.compile('\d+\.?\d+')
r = re.compile(r"""
    \d+ # 小数点前面的数字
    \.? # 小数点本身
    \d+ # 小数点后面的数字
""",re.VERBOSE)
ret = re.search(r,text)
print(ret.group())





















