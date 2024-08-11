from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium import webdriver

def test_wge():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(10)
    ele = driver.find_element(locate_with(By.XPATH,"//a").to_left_of({By.LINK_TEXT: "网盘"}))
    ele.click()
    sleep(3)