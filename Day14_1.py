from requests import get
from bs4 import BeautifulSoup

response = get('https://janet.co.kr/')
print(response.status_code)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.name')

for title in titles:
   print(title.text)
