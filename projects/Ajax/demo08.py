from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

# selenium中的WebElement类的补充


driver_path = r'E:\Python\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')


# submitTag = driver.find_element_by_id('su')
# print(submitTag.get_attribute('value'))


driver.save_screenshot('baidu.png')


