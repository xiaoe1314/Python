"""
    Created by 朝南而行 2019/3/8 10:32
"""
import os
import time
import csv


class Controller(object):
    def __init__(self, count):
        self.count = count
        self.addData = [("timestamp", "cpustatus")]

    # 单次测试过程
    def testProcess(self):
        result = os.popen('adb shell " dumpsys cpuinfo | grep com.blackfish.app.ui"')
        cpuValue = ''
        for line in result:
            cpuValue = line.split('%')[0]
            break


        currentTime = self.getCurrentTime()
        self.addData.append((currentTime, cpuValue))
        print(currentTime+'==='+cpuValue)
        print('*' * 100)

    # 多次测试过程
    def run(self):
        while self.count > 0:
            self.testProcess()
            self.count = self.count - 1
            time.sleep(5)

    # 获取当前的时间戳
    @staticmethod
    def getCurrentTime():
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    def saveDataToCsv(self):
        with open('cpustatus.csv', 'w', newline='') as fp:
            writer = csv.writer(fp)
            writer.writerows(self.addData)


if __name__ == '__main__':
    controller = Controller(10)
    controller.run()
    controller.saveDataToCsv()
