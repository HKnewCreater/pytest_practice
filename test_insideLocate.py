from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

def test_insideloc():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(10)
    ele = driver.find_elements(By.XPATH,"//div[@id='s-top-left']//a")
    ele[6].click()
    sleep(3)