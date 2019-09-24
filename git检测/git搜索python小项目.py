import requests

get_code_api = "https://api.github.com/search/code?q="
get_repo_api = "https://api.github.com/search/repositories?q=language:python"


def get_code(language, size, repo):
    url = get_code_api + "language:" + language + "+size:" + size + "+repo:" + repo
    info = requests.get(url).json()
    if 'items' in info:
        for i in info['items']:
            print(i['html_url'])


def get_project(last_week):
    info = requests.get(get_repo_api).json()
    for i in info['items']:
        created_time = i['created_at']
        if created_time > last_week:
            language = "python"
            size = "<200"
            repo = i['html_url'].replace("https://github.com/", "")
            get_code(language, size, repo)


get_project("2018-03-3T00:00:00Z")
