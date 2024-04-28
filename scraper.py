from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

print(soup.prettify())
print(soup.title)

divs = soup.find_all('div')
for div in divs:
    print(div)