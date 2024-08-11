from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_cshot():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.maximize_window()
    driver.find_element(By.ID,"kw").send_keys("福建")
    driver.find_element(By.ID,"su").click()
    print(driver.get_screenshot_as_png())
    sleep(3)
    driver.close()