import time
from selenium import webdriver


def start_chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver


def find_strangers():
    btn_sel = 'div.ContentItem-extra > button.Button--blue'
    elems = driver.find_elements_by_css_selector(btn_sel)
    return elems


while True:
    url = 'https://www.zhihu.com/'
    follower_url = 'https://www.zhihu.com/people/xxx/followers'  # 需替换成你的知乎url，点击【我的主页】→【关注者】可进入该页面
    driver = start_chrome()
    driver.get(url)
    if not driver.get_cookie():
        print('再次登陆')
    time.sleep(20)
    driver.get(follower_url)
    time.sleep(6)
    strangers = find_strangers()
    for s in strangers:
        s.click()
        time.sleep(3)
    print('Done!')
    time.sleep(300)
