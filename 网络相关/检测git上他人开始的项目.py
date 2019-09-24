import requests
import webbrowser
import time

# 修改name检测不同作者
name = 'kennethreitz'
api = 'https://api.github.com/users/%s/starred' % name
info = requests.get(api).json()
# 项目id列表
starred = []

# 获取项目id
for i in info:
    starred.append(i['id'])

while True:
    info = requests.get(api).json()
    # 更新数据进行对比取出不同打开新项目
    for i in info:
        if not i['id'] in starred:
            starred.append(i['id'])
            repo_name = i['name']
            owner = i['owner']['login']
            web_page = 'https://github.com/%s/%s' % (owner, repo_name)
            webbrowser.open(web_page)
    time.sleep(600)
