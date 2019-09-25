import time
from selenium import webdriver


def start_chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver


def get_info(driver, url):
    driver.get(url)
    time.sleep(6)
    sel = "//*[@id=\"pl_topic_header\"]/div[2]/div[3]/div/div[2]/span[2]"
    elems = driver.find_element_by_xpath(sel)
    result = elems.text.replace('讨论', '')
    return result


url = "https://s.weibo.com/weibo/%2523%25E5%25A5%25A5%25E6%2596%25AF%25E5%258D%25A1%2523&Refer=STopic_box"
driver = start_chrome()
target = '370万'
while True:
    result = get_info(driver, url)
    if result >= target:
        print(f'讨论超过{result}')
        break
    else:
        print('未达到')
    time.sleep(1200)
print('Done!')
