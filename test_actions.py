from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_acChain():
    driver = webdriver.Chrome()
    driver.get("https://www.csdn.net/")
    driver.maximize_window()
    ele = driver.find_element(By.XPATH,"//*[text()='历史']")
    actionChains = ActionChains(driver)
    actionChains.move_to_element(ele).perform()
    sleep(3)