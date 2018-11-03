import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
gTimes = 0


# 生产者
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while gTimes < 10:
            money = random.randint(100, 1000)
            gLock.acquire()
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            gLock.release()
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
                time.sleep(1)
            else:
                print('没有足够的金钱')
            gLock.release()


def main():
    for x in range(5):
        t = Producer(name='生产者%d' % x)
        t.start()

    for x in range(3):
        t = Consumer(name='消费者%d' % x)
        t.start()


if __name__ == '__main__':
    main()