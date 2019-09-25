from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os


def start_chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver


def q(st, et):
    return f'?is_ori=1&key_word=&start_time={st}&end_time={et}&is_search=1&is_searchadv=1#_0'


def scroll_down():
    html_page = driver.find_element_by_tag_name('html')
    for i in range(15):
        html_page.send_keys(Keys.END)
        time.sleep(0.6)


def find_cards_info():
    cards_sel = 'div.WB_feed_detail'
    cards = driver.find_elements_by_css_selector(cards_sel)
    info_list = []

    for card in cards:
        content_sel = 'div.WB_text.W_f14'
        time_sel = 'div.WB_from.S_txt2'
        link_sel = 'div.WB_from.S_txt2 > a:nth-child(1)'

        content = card.find_element_by_css_selector(content_sel).text
        time = card.find_element_by_css_selector(time_sel).text
        link = card.find_element_by_css_selector(link_sel).get_attribute('href')
        info_list.append([content, time, link])
    return info_list


def find_next():
    next_sel = 'a.page.next'
    next_page = driver.find_elements_by_css_selector(next_sel)
    if next_page:
        return next_page[0].get_attribute('href')


def save(info_list, name):
    full_path = name + '.csv'
    if os.path.exists(full_path):
        w = 'a'
    else:
        w = 'w+'
    with open(full_path, w, ) as f:
        writer = csv.writer(f)
        writer.writerows(info_list)
        print('Done')


def run_crawler(base, duration):
    if not base.endswith('feedtop'):
        st, et = duration.split('~')
        driver.get(base + q(st, et))
    else:
        driver.get(base)
    time.sleep(5)
    scroll_down()
    time.sleep(5)
    info_list = find_cards_info()
    save(info_list, duration)
    next_page = find_next()
    if next_page:
        run_crawler(next_page, duration)


base = 'https://weibo.com/u/3511727907'
driver = start_chrome()
input()
run_crawler(base, '2018-06-20~2019-02-03')
