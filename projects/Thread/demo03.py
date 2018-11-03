import threading


VALUE = 0
# 给线程加锁（防止同时执行，像上厕所一样，关着门，后面的人要排队）
gLock = threading.Lock()


def add_value():
    global VALUE
    # 加锁
    gLock.acquire()
    # 会产生同时在执行的情况
    for x in range(1000000):
        # 想引用全局的值或者改变，需要用global声明
        VALUE += 1
    # 释放锁
    gLock.release()
    print('value: %d' % VALUE)


def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()


if __name__ == '__main__':
    main()
