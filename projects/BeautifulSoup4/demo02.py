
from bs4 import BeautifulSoup

html = """
<tbody>
<tr class="h">
    <td class="l" width="374">职位名称</td>
    <td>职位类别</td>
    <td>人数</td>
    <td>地点</td>
    <td>发布时间</td>
</tr>
<tr class="even">
    <td class="l square"><a target="_blank" href="position_detail.php?id=43639&amp;keywords=&amp;tid=87&amp;lid=0">SA-腾讯社交广告测试开发工程师（研发中心
        北京）</a></td>
    <td>技术类</td>
    <td>1</td>
    <td>北京</td>
    <td>2018-08-24</td>
</tr>
<tr class="odd">
    <td class="l square"><a target="_blank" href="position_detail.php?id=43622&amp;keywords=&amp;tid=87&amp;lid=0">25923-游戏高级技术运营工程师（深圳）</a>
    </td>
    <td>技术类</td>
    <td>1</td>
    <td>深圳</td>
    <td>2018-08-24</td>
</tr>
<tr class="even">
    <td class="l square"><a target="_blank" href="position_detail.php?id=43619&amp;keywords=&amp;tid=87&amp;lid=0">22989-高级Web前端开发工程师（深圳）</a>
    </td>
    <td>技术类</td>
    <td>1</td>
    <td>深圳</td>
    <td>2018-08-24</td>
</tr>
<tr class="odd">
    <td class="l square"><a target="_blank" href="position_detail.php?id=43611&amp;keywords=&amp;tid=87&amp;lid=0">SNG04-内容后台开发工程师(深圳)</a>
    </td>
    <td>技术类</td>
    <td>2</td>
    <td>深圳</td>
    <td>2018-08-24</td>
</tr>
<tr class="even">
    <td class="l square"><a target="_blank" href="position_detail.php?id=43612&amp;keywords=&amp;tid=87&amp;lid=0">SNG04-内容算法工程师(深圳)</a>
    </td>
    <td>技术类</td>
    <td>2</td>
    <td>深圳</td>
    <td>2018-08-24</td>
</tr>
<tr class="odd">
    <td class="l square"><a target="_blank" href="position_detail.php?id=43604&amp;keywords=&amp;tid=87&amp;lid=0">25925-Android开发工程师（深圳）</a>
    </td>
    <td>技术类</td>
    <td>1</td>
    <td>深圳</td>
    <td>2018-08-24</td>
</tr>
<tr class="even">
    <td class="l square"><a target="_blank" href="position_detail.php?id=43606&amp;keywords=&amp;tid=87&amp;lid=0">MIG03-车联网车厂合作项目品质管理工程师（北京）</a><span
            class="hot">&nbsp;</span></td>
    <td>技术类</td>
    <td>1</td>
    <td>北京</td>
    <td>2018-08-24</td>
</tr>
<tr class="odd">
    <td class="l square"><a target="_blank" href="position_detail.php?id=43591&amp;keywords=&amp;tid=87&amp;lid=0">22989-腾讯云SMB业务售前架构师（北京/上海/深圳/成都）</a>
    </td>
    <td>技术类</td>
    <td>2</td>
    <td>深圳</td>
    <td>2018-08-24</td>
</tr>
<tr class="even">
    <td class="l square"><a target="_blank" href="position_detail.php?id=43594&amp;keywords=&amp;tid=87&amp;lid=0">MIG09-浏览器大资讯后台开发高级工程师（北京）</a>
    </td>
    <td>技术类</td>
    <td>1</td>
    <td>深圳</td>
    <td>2018-08-24</td>
</tr>
<tr class="odd">
    <td class="l square"><a id='test' class='test' target="_blank" href="position_detail.php?id=43596&amp;keywords=&amp;tid=87&amp;lid=0">21309-在线教育c++/java/go后台高级研发工程师(深圳)</a>
    </td>
    <td>技术类</td>
    <td>2</td>
    <td>深圳</td>
    <td>2018-08-24</td>
</tr>
</tbody>
"""

# 1.获取所有的tr标签
# 2.获取第二个tr标签
# 3.获取所有的class等于even的tr标签
# 4.将所有id等于test class等于test的标签提前出来(css选择实现不了，只能选一个)
# 5.获取所有的a标签
# 6.获取所有的职位信息

soup = BeautifulSoup(html,'lxml')

# 1.获取所有的tr标签
# trs = soup.select('tr')
# for tr in trs:
#     print(tr)

# 2.获取第二个tr标签
# tr = soup.select('tr')[1]
# print(tr)

# 3.获取所有的class等于even的tr标签
# trs = soup.select('.even')
# trs = soup.select("tr[class='even']")
# for tr in trs:
#     print(tr)

# 5.获取所有的a标签
# trs = soup.select('a')
# for tr in trs:
#     href = tr['href']
#     print(href)

# 6.获取所有的职位信息
#列表
movies = []
trs = soup.select('tr')
for tr in trs:
    # 字典
    movie = {}
    infos = list(tr.stripped_strings)
    movie['title'] = infos[0]
    movie['category'] = infos[1]
    movie['nums'] = infos[2]
    movie['city'] = infos[3]
    movie['time'] = infos[4]
    movies.append(movie)
print(movies)






