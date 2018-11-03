from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# selenium的隐式等待和显示等待

driver_path = r'E:\Python\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com')


# 隐式等待：调用driver.implicitly_wait。那么在获取不可用的元素之前，会先等待10秒中的时间。
# driver.implicitly_wait(10)
# driver.find_element_by_id('123456456')

# 显示等待：显示等待是表明某个条件成立后才执行获取元素的操作。也可以在等待的时候指定一个最大的时间，
# 如果超过这个时间那么就抛出一个异常。显示等待应该使用selenium.webdriver.support.excepted_conditions期望的条件
# 和selenium.webdriver.support.ui.WebDriverWait来配合完成

element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, 'form_email'))
)
print(element)
