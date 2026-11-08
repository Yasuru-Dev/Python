from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

#user agent header
#this need for web scriping from wikipedia
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'
}

page=requests.get(url, headers=headers)
soup=BeautifulSoup(page.text, 'html.parser')
print(soup)