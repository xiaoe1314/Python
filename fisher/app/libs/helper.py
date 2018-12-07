"""
    Created by 朝南而行 2018/12/5 16:36
"""


def is_isbn_or_key(word):
    # isbn: isbn13 13个0到9的数字组成
    # isbn: isbn10 10个0到9的数字组成,含有 '-'
    isbn_or_key = 'key'
    # q.isdigit()是不是全部由数字组成
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_q = word.replace('-', '')
    if '-' in word and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
