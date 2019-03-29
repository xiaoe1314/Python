import csv

# 通过下标读取文件
# def read_csv_demo():
#     with open('', 'r') as fp:
#         # reader是一个迭代器
#         reader = csv.reader(fp)
#         # next 会对迭代器会从开始位置加一位
#         next(reader)
#         for x in reader:
#             name = [3]
#             other = [-1]
#             print({'name': name, 'other': other})


# 通过字典读取文件
def read_csv_demo2():
    a = []
    with open('classroom2.csv', 'r') as fp:
        # 使用DictReader创建的reader对象
        # 不会包含的那行数据
        reader = csv.DictReader(fp)
        for x in reader:
            value = {'username': x['username'], 'age': x['age']}
            e = (value['username'], value['age'])
            a.append(e)
    return a

# 通过写入文件
# def read_csv_demo3():
#     headers = ['username', 'age', 'height']
#
#     values = [
#         {'张三', '18', '156'},
#         {'李四', '19', '184'},
#         {'王五', '20', '168'}
#     ]
#
#     # newline 是写入一行后做的事
#     with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
#         writer = csv.writer(fp)
#         # 写入表头
#         writer.writerow(headers)
#         # 写入数据
#         writer.writerows(values)
#
#
# # 通过字典写入文件
# def read_csv_demo4():
#     headers = ['username', 'age', 'height']
#
#     values = [
#         {'username':'张三', 'age':18, 'height':156},
#         {'username':'李四', 'age':19, 'height':184},
#         {'username':'王五', 'age':20, 'height':168}
#     ]
#     # newline 是写入一行后做的事
#     with open('classroom2.csv', 'w', encoding='utf-8', newline='') as fp:
#         writer = csv.DictWriter(fp,headers)
#         # 写入表头数据的时候，需要执行writeheader函数
#         writer.writeheader()
#         writer.writerows(values)
#
#


if __name__ == '__main__':
    print(read_csv_demo2())

