from queue import Queue
import time
import threading

# Queues是线程安全的队列
# 初始化Queue(maxsize)：创建一个先进先出的队列。
# qsize()：返回队列的大小。
# empty()：判断队列是否为空。
# full()：判断队列是否满了。
# get()：从队列中取最后一个数据。get()默认里面的参数block=True，
# block是指当前的操作是阻塞式的，从队列获取值，如果队列没有值则一直阻塞着，直到队列获取不到为止
# put()：将一个数据放到队列中。put()默认里面的参数block=True，
# block是指当前的操作是阻塞式的，从队列添加值，如果队列已经满了则一直阻塞着，直到队列不满为止

# q = Queue(4)
# for x in range(4):
#     print(x)
# for x in range(4):
#     print(q.get())


def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(3)


def get_value(q):
    while True:
        print(q.get())


def main():
    q = Queue(4)
    t1 = threading.Thread(target=set_value,args=[q])
    t2 = threading.Thread(target=get_value,args=[q])

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()



















