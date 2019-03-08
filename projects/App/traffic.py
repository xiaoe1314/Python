"""
    Created by 朝南而行 2019/3/8 10:32
"""
import os
import time
import csv


# 流量监测消耗
class Controller(object):
    def __init__(self, count):
        self.count = count
        self.addData = [("timestamp", "traffic")]
        self.receive = '0'
        self.transmit = '0'
        self.receive2 = '0'
        self.transmit3 = '0'

    # 单次测试过程
    def testProcess(self):
        result = os.popen('adb shell "ps | grep com.android.browser"')
        # result = os.popen('adb shell "ps | grep  com.blackfish.app.ui"')

        # 获取进程ID
        pid = result.readlines()[0].split(' ')[4]

        # 获取进程ID使用的流量
        traffic = os.popen('adb shell cat /proc/' + pid + '/net/dev')

        for line in traffic:
            # print(line)
            if 'eth0' in line:
                # 将所有的空格换成#
                line = '#'.join(line.split())
                # 获取收到和发出的流量
                self.receive = line.split('#')[1]
                self.transmit = line.split('#')[9]
            elif 'eth1' in line:
                # 将所有的空格换成#
                line = '#'.join(line.split())
                # 获取收到和发出的流量
                self.receive2 = line.split('#')[1]
                self.transmit2 = line.split('#')[9]
                print(self.receive2 + '===' + str(self.transmit2))

        # 计算所有流量之和
        allTraffic = (int(self.receive) + int(self.transmit) + int(self.receive2) + int(self.transmit2))/1024
        currentTime = self.getCurrentTime()
        self.addData.append((currentTime, str(int(allTraffic))))
        print(currentTime+'==='+str(allTraffic))
        print('*' * 100)

    # 多次测试过程
    def run(self):
        while self.count > 0:
            self.testProcess()
            self.count = self.count - 1
            time.sleep(3)

    # 获取当前的时间戳
    @staticmethod
    def getCurrentTime():
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    def saveDataToCsv(self):
        with open('traffic.csv', 'w', newline='') as fp:
            writer = csv.writer(fp)
            writer.writerows(self.addData)


if __name__ == '__main__':
    controller = Controller(5)
    controller.run()
    # 得出的数据拿最后一个减第一个
    controller.saveDataToCsv()