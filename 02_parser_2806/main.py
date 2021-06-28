import requests
import pandas as pd
from bs4 import BeautifulSoup
from my_parser import *
# ^ это мой файл, в котором будет функция парсинга

url = ''
connect = requests.get(url)
df = pd.DataFrame()
soup = BeautifulSoup(connect.text, features='html.parser')
cards = ''

for item in cards:
    s = parse_dominos(item)
    df = df.append(s, ignore_index=True)

df.to_excel('dominos.xlsx')