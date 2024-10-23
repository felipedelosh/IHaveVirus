"""
OPEN PAGE IN MULTIPLE TIMES
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)

_url = "https://chatgpt.com/"


for _ in range(1000000):
    try:
        driver.get(_url)
    except:
        pass
    time.sleep(0.4)


driver.quit()
