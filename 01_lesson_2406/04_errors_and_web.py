import requests

url = [
    'https://vk.com/',
    'https://api.github.com/',
    'https://redtool.by/',
    'https://gjhfjgkhf.com/'
]

for url in url:
    try:
        call = requests.get(url)
        print(url, 'успех', call.status_code)
    except:
        print(url, 'Что-то пошло не так!')