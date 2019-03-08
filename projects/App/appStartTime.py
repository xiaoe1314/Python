"""
    Created by 朝南而行 2019/3/8 10:32
"""
import os
import time
import csv


class App(object):
    def __init__(self):
        self.content = None
        self.startTime = ''

    def launchApp(self):
        cmd = 'adb shell am start -W -n com.blackfish.app.ui/cn.blackfish.host.splash.WelcomeActivity'
        # 使用 os.popen(cmd) 执行命令
        self.content = os.popen(cmd)
        print(self.content)

    @staticmethod
    def forceStopAPP():
        # cmd = 'adb shell am force-stop com.blackfish.app.ui'
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)

    def getLaunchedTime(self):
        for line in self.content.readlines():
            print(line)
            if 'ThisTime' in line:
                self.startTime = line.split(':')[-1]
                break
        return self.startTime


class Controller(object):
    def __init__(self, count):
        self.app = App()
        self.count = count
        self.addData = [("timestamp", "elapsedtime")]

    # 单次测试过程
    def testProcess(self):
        self.app.launchApp()
        time.sleep(5)
        elapsedtime = self.app.getLaunchedTime()
        self.app.forceStopAPP()
        time.sleep(3)
        currentTime = self.getCurrentTime()
        self.addData.append((currentTime, elapsedtime))

    # 多次测试过程
    def run(self):
        while self.count > 0:
            self.testProcess()
            self.count = self.count - 1

    # 获取当前的时间戳
    @staticmethod
    def getCurrentTime():
        currentTime = time.strftime("%Y-%M-%D %H:%M:%S", time.localtime())
        return currentTime

    def saveDataToCsv(self):
        with open('test.csv', 'w', newline='') as fp:
            writer = csv.writer(fp)
            writer.writerows(self.addData)


if __name__ == '__main__':
    controller = Controller(10)
    controller.run()
    controller.saveDataToCsv()
