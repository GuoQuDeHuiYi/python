import requests
import time


# 发送信息
def push_it(message):
    api = 'https://api.pushover.net/1/messages.json/'
    data = {
        'app_token': '',
        'user': '',
        'message': message
    }
    requests.post(api, data)


# 获取新库
def get_project(last_week, topic):
    api = 'https://api.github.com/search/repositories?q='
    query_created = 'created:>' + last_week
    query_topic = 'topic:' + topic
    r = requests.get(api + query_created + '+' + query_topic)
    return r.json()['items']


last_week = "2018-03-3T00:00:00Z"
topic = 'blockchain'

result = []
while True:
    project_list = get_project(last_week, topic)
    for p in project_list:
        stars = p['stargazers_count']
        if stars > 200 and not p['html_url'] in result:
            message = 'The project' + p['name'] + 'is qualified' + 'URL:' + ['html_url']
            push_it(message)
            result.append(p['html_url'])
    time.sleep(600)
