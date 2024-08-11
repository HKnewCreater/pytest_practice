from time import sleep
from selenium import webdriver

def test_roll():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(10)
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1200, height)
    current_position = 0
    scroll_step = 80
    driver.implicitly_wait(10)

    while current_position < height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        current_position += scroll_step
        sleep(0.1)  # 稍微等待一下，让页面加载内容

    driver.save_screenshot('MouseRoll.png')
    sleep(3)
    driver.quit()
