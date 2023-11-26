import requests
from bs4 import BeautifulSoup

url = 'https://market.mosreg.ru/Trade'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

categories = soup.find_all('span', class_='CategoryName')
for category in categories:
    print(category.text)
