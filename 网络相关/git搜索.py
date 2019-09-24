# https://api.github.com/search/repositories?q=
# https://api.github.com/search/repositories?q=topic:

import requests


def get_names():
    # 获取搜索信息
    names = input('输入搜索信息:')
    return names.split()


def check_repos(names):
    # git开放api
    repo_api = 'https://api.github.com/search/repositories?q='
    ecosys_api = 'https://api.github.com/search/repositories?q=topic:'
    # 搜索并取出需要的数据
    for name in names:
        repo_info = requests.get(repo_api + name).json()['items'][0]
        stars = repo_info['stargazers_count']
        forks = repo_info['forks_count']
        ecosys_info = requests.get(ecosys_api).json()['total_count']

        print(name)
        print('Stars:' + str(stars))
        print('Forks:' + str(forks))
        print('Ecosys:' + str(ecosys_info))
        print('-' * 10)


names = get_names()
check_repos(names)
