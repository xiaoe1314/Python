from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# 常见的表单元素 input type='text/password/email/number'
# button/input type='submit'
# checkbox input='checkbox'
# select 下拉列表


driver_path = r'E:\Python\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# 1: 操作input
# 打开浏览器的一个网页
# driver.get('https://www.baidu.com')
# inputTag = driver.find_elements_by_id('kw')[0]
# # 发送(输入)数据
# inputTag.send_keys('python')
# time.sleep(3)
# # 清除（删除）数据
# inputTag.clear()


# 2: 操作checkbox
# 打开浏览器的一个网页
# driver.get('https://www.douban.com')
# checkboxTag = driver.find_element_by_name('remember')
# # checkbox 点击选项框(点击一次click就选中)
# checkboxTag.click()
# time.sleep(3)
# # checkbox 取消选项框(点击二次click就选中)
# checkboxTag.click()


# 3: 操作select（下拉列表）
# 打开浏览器的一个网页
# driver.get('http://www.17sucai.com/pins/demo-show?id=9673')
# selectTag = Select(driver.find_element_by_class_name('selectbox'))
# selectTag.select_by_index(2)
# selectTag.deselect_by_value('')
# selectTag.deselect_by_visible_text('CSS3')
# selectTag.deselect_all()

# 4: 按钮点击事件
# 打开浏览器的一个网页
driver.get('https://www.baidu.com')
inputTag = driver.find_element_by_id('kw')
# 发送(输入)字符串
inputTag.send_keys('python')

submitTag = driver.find_element_by_id('su')
# 执行点击事件
submitTag.click()

