"""
    Created by 朝南而行 2018/12/13 16:20
"""


# 第一版代码
# class BookViewModel:
#     # 没有面向对象
#     # 只描述了行为，没有描述特性（实质还是面向过程）
#     @classmethod
#     def package_single(cls, data, keyword):
#         returned = {
#             'total': 0,
#             'keyword': keyword,
#             'books': []
#         }
#         if data:
#             returned['total'] = 1
#             returned['books'] = [cls.__cut_book_data(data)]
#
#         return returned
#
#     @classmethod
#     def package_collection(cls, data, keyword):
#         returned = {
#             'total': 0,
#             'keyword': keyword,
#             'books': []
#         }
#         if data:
#             returned['total'] = data['total']
#             # 列表推导式
#             returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
#
#         return returned
#
#     @classmethod
#     def __cut_book_data(cls, data):
#         book = {
#             'title': data['title'],
#             'publisher': data['publisher'],
#             'pages': data['pages'] or '',
#             'author': '、'.join(data['author']),  # 列表转换为字符串  '、'.join(list) 通过、分割列表中的每一项
#             'price': data['price'],
#             'summary': data['summary'] or '',
#             'image': data['image'],
#         }
#         return book

# 第二版代码
class BookViewModel:
    # 修改为面向对象
    # 描述特征 （类变量、实例变量）
    # 行为 （方法）
    # 找到调用的源头 YuShuBook, 关键的词是book,描述书籍
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.author = '、'.join(book['author'])  # 列表转换为字符串  '、'.join(list) 通过、分割列表中的每一项
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.keyword = ''
        self.books = []

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


