from bs4 import BeautifulSoup
import requests

url = 'https://www.singersl.com/'
page=requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')
print(soup)