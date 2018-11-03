from selenium import webdriver

# 获取cookie信息

driver_path = r'E:\Python\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')

for cookie in driver.get_cookies():
    print(cookie)


# 根据cookie的键为name的值传入(删除对应name值的cookie)
driver.delete_cookie('BAIDUID')

# 删除全部cookie
driver.delete_all_cookies()

print('='*100)
# 根据cookie的键为name的值传入
print(driver.get_cookie('BAIDUID'))
