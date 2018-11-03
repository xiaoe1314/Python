
import threading
import time

# 继承自threading.Thread类实现多线程
class CodingClass(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在写代码%s' % threading.current_thread())
            time.sleep(1)


class DrawingClass(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在画图%s' % threading.current_thread())
            time.sleep(1)


def main():
    t1 = CodingClass()
    t2 = DrawingClass()

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()