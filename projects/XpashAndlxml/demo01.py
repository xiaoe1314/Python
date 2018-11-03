from lxml import etree

# 1.获取所有的标签
# 2.获取第2个标签
# 3.获取所有class等于even的标签
# 4.获取所有按标签的href属性
# 5.获取躲雨的职位信息（纯文本）

parserHtml = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tencent.html',parser=parserHtml)

# 1.获取所有的tr标签
# //tr
# xpath函数返回一个列表
#     trs = html.xpath('//a/@href')
#     for tr in trs:
#         print('https://hr.tencent.com/'+tr)

trs = html.xpath('//tr[position()>1]')
positions = []
for tr in trs:
    href = tr.xpath('.//a/@href')[0]
    fullurl = 'https://hr.tencent.com/'+href
    title = tr.xpath('.//td[1]//text()')[0]
    category = tr.xpath('.//td[2]//text()')[0]
    nums = tr.xpath('.//td[3]//text()')[0]
    address = tr.xpath('.//td[4]//text()')[0]
    pubtime = tr.xpath('.//td[5]//text()')[0]

    position = {
        'url' : fullurl,
        'title' : title,
        'category' : category,
        'nums' : nums,
        'address' : address,
        'pubtime' : pubtime
    }

    positions.append(position)

print(positions)
