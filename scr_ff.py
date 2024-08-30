import datetime
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException

url = "https://www.biccamera.com/bc/category/?q=SSD"
#url = "https://www.microsoft.com"
#url = "https://news.google.com/home?hl=ja&gl=JP&ceid=JP:ja"
#url = "https://www.yahoo.co.jp/"
#url = "https://www.google.com"
#url = "https://www.edion.com/item_list.html?keyword=HDD"

service = Service(log_output=r"geckodriver.log")
options = Options()
options.log.level = "trace"
options.add_argument("--headless")
#options.set_preference('javascript.enabled', False)
#options.set_preference("privacy.trackingprotection.enabled", True)
#options.set_preference("browser.cache.disk.enable", False)
#options.set_preference("browser.cache.memory.enable", False)
#options.set_preference("browser.cache.offline.enable", False)
#options.set_preference("network.http.use-cache", False)
#options.set_preference('network.cookie.cookieBehavior', 2)
driver = webdriver.Firefox(service=service, options=options)

driver.set_page_load_timeout(300)
driver.set_script_timeout(30)
driver.delete_all_cookies()

driver.execute_script('const newProto = navigator.__proto__;delete newProto.webdriver;navigator.__proto__ = newProto;')

#time.sleep(30)

try:
    print(datetime.datetime.now())
    print(driver.execute_script('return navigator.webdriver'))
    driver.get(url)
except TimeoutException as e:
    print("Exception occures!")
finally:
    print(datetime.datetime.now())
    print("readyState=" + driver.execute_script('return document.readyState'))

test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
for item in test:
    print(item)

total_width = driver.execute_script("return document.body.offsetWidth")
total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
driver.set_window_size(int(total_width), int(total_height))
driver.save_screenshot(r'screenshot.png')

driver.quit()
