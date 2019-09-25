import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions

url = 'https://weibo.com/5869525717/G2VASlH1o?from=page_1005055869525717_profile&wvr=6&mod=weibotime&type=comment'  # 可以替换成你想跟踪的单条微博链接


def start_chrome():
    options = ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(chrome_options=options)
    driver.start_client()
    return driver


def find_find():
    sel = 'span > span.line.S_line1 > span > em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text) for el in elems[1:]]


while True:
    driver = start_chrome()
    driver.get(url)
    time.sleep(6)
    info = find_find()
    rep, comm, like = info
    if rep > 30000:
        print(f'你喜欢的微博转发量已经到达{rep}条')
        break
    else:
        print('Not happening')
    time.sleep(1200)

print('Done!')
