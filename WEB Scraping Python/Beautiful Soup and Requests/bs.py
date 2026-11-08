from bs4 import BeautifulSoup
import requests

url = 'https://www.singersl.com/'
page=requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')
print(soup.prettify())

soup2=soup.find_all('div')
print(soup2)

soup3=soup.finall('p')
print(soup3)