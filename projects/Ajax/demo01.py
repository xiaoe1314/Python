
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#Selenium+chromedriver获取动态数据
driver_path = r'E:\Python\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
# 打开浏览器的一个网页
driver.get('https://www.baidu.com')

# 1:
# 通过page_source获取网页源代码
#print(driver.page_source)
# time.sleep(5)
# 关闭整个浏览器
# driver.quit()
# 关闭一个页面
# driver.close()

# 2:
# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element_by_name('wd')
# inputTag = driver.find_element_by_class_name('s_ipt')
# inputTag = driver.find_element_by_xpath("//input[@id='kw']")
# inputTag = driver.find_element_by_css_selector(".quickdelete-wrap > input")
# inputTag = driver.find_elements_by_css_selector(".quickdelete-wrap > input")[0]
inputTag = driver.find_elements(By.CSS_SELECTOR,".quickdelete-wrap > input")[0]
# 发送(输入)字符串
inputTag.send_keys('python')







