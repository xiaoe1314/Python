from selenium import webdriver

# selenium使用代理

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://117.90.3.112:8010")

driver_path = r'E:\Python\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
driver.get('http://httpbin.org/ip')

