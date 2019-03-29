"""
    Created by 朝南而行 2019/3/29 10:52
"""
import csv


def read_csv():
    a = []
    with open('classroom2.csv', 'r') as fp:
        # 使用DictReader创建的reader对象
        # 不会包含的那行数据
        reader = csv.DictReader(fp)
        for x in reader:
            e = (x['name'], x['pwd'])
            a.append(e)
    return a
