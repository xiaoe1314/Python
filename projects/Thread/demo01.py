
import time
import threading

# 传统的写法
# def coding():
#     for x in range(3):
#         print('正在写代码%s'%x)
#         time.sleep(1)
#
#
# def drawing():
#     for x in range(3):
#         print('正在画图%s' % x)
#         time.sleep(1)


# 多线程的写法
def coding():
    for x in range(3):
        print('正在写代码%s' % threading.current_thread())
        time.sleep(1)


def drawing():
    for x in range(3):
        print('正在画图%s' % threading.current_thread())
        time.sleep(1)


def main():
    # 创建子线程（指定函数执行,加圆括号是返回值）
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

    # 查看进程中的线程数
    print(threading.enumerate())
    # 查看进程中的线程名 threading.current_thread()


if __name__ == '__main__':
    main()