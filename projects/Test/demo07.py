"""
    Created by 朝南而行 2019/4/11 11:17
"""

import os
import time

def a():
    # lisenter = 'adb shell "logcat | grep cmp="'
    # mlisenter = os.popen(lisenter)
    # time.sleep(2)
    # cmd = 'adb shell am start -W -n com.jianzhiku.zhongrenbang/com.jianzhiku.activity.StartActivity'
    # # # 使用 os.popen(cmd) 执行命令
    # time.sleep(10)
    # os.popen(cmd)
    # time.sleep(10)
    #
    # a = 'adb logcat'
    # print(os.popen(a))
    # # print(content, end='\n' + '='*100)
    # # print(mlisenter)

    activityNowCmd = 'adb shell "dumpsys activity activities | grep mResumedActivity"'
    # activityNowCmd = 'ipconfig'
    activityNow = os.popen(activityNowCmd).readlines()
    # activityNow = os.system(activityNowCmd).readlines()
    print(type(activityNow))
    print(len(activityNow))
    print(activityNow[0].split('/')[-1].split(' ')[0])

    a = activityNow[0].split('/')[-1].split(' ')[0]

    if 'com.jianzhiku.activity.GuideActivity' == str(a):
        print('666')


    # for x in a
    # if len(activityNow) == 1:
    #     content = activityNow
    #     a = content.split('/').split(' ')
    #     print(type(content))
    #     print(a)


a()