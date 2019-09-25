import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def start_chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    driver.set_window_size(1500, 1500)
    return driver


def login(driver, url):
    driver.get(url)
    time.sleep(25)


def click_lisk(driver, url, have_clicked):
    driver.get(url)
    time.sleep(6)
    weibo_sel = '#Pl_Official_MyProfileFeed__21 > div > div'
    weibo_elems = driver.find_elements_by_css_selector(weibo_sel)
    for w in weibo_elems:
        time_sel = 'div.WB_feed_detail > div.WB_detail > div.WB_from.S_txt2 > a:nth-child(1)'
        weibo_time = w.find_elements_by_css_selector(time_sel)
        if len(weibo_time) == 1:
            weibo_time = weibo_time[0].text
        if weibo_time not in have_clicked:
            button_sel = 'div.WB_feed_handle > div > ul > li:nth-child(4) > a > span > span > span'
            button = w.find_elements_by_css_selector(button_sel)
            if len(button) == 1:
                button = button[0]
                try:
                    button.click()
                except Exception:
                    html_page = driver.find_element_by_tag_name('html')
                    html_page.send_keys(Keys.DOWN)
                    button.click()
                have_clicked.append(weibo_time)
                print(have_clicked)
                time.sleep(5)


login_url = 'https://weibo.com/'
weibo_url = 'https://weibo.com/bgsxy'
have_clicked = []
driver = start_chrome()
login(driver, login_url)
while True:
    have_clicked = click_lisk(driver, weibo_url, have_clicked)
    time(1200)
