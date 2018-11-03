from selenium import webdriver

# selenium打开窗口和切换窗口

driver_path = r'E:\Python\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')
# driver.get('https://www.douban.com')


# 可以执行JavaScript代码(打开多窗口)
driver.execute_script("window.open('https://www.douban.com/')")

print(driver.window_handles)
# 虽然在窗口中切换到新的页面，但是driver中还没有切换到新的页面
# 如果想在代码中切换到新的页面，并且做一些爬虫
# 那么应该使用switch_to_window来切换到指定页面
# 从driver.window_handles中取出具体的第几个窗口
# 他会按照打开页面的顺序来存储窗口的句柄

# switch_to_window切换窗口
driver.switch_to_window(driver.window_handles[1])
# current_url是当前指向的url
print(driver.current_url)




