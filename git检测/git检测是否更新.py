# api https://api.github.com/repos/channelcat/sanic
# web_page https://github.com/channelcat/sanic

import requests
import webbrowser
import time

# github公开的接口
api = 'https://api.github.com/repos/channelcat/sanic'
# 发现更新打开的网址
web_page = 'https://github.com/channelcat/sanic'

# 之前的更新时间
last_update = None
# 获取数据
all_info = requests.get(api).json()
# 取出更新时间
cur_update = all_info['updated_at']
# print(cur_update)

while True:
    if not last_update:
        last_update = cur_update

    if last_update < cur_update:
        webbrowser.open(web_page)
    time.sleep(600)
