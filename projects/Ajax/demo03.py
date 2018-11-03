
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 行为链

driver_path = r'E:\Python\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')

inputTag = driver.find_element_by_id('kw')
submitTag = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, 'python')
actions.move_to_element(submitTag)
actions.click(submitTag)
actions.perform()

# 点击不松开鼠标
# actions.click_and_hold(submitTag)
# 右键点击
# actions.context_click(submitTag)
# 双击
# actions.double_click(submitTag)
