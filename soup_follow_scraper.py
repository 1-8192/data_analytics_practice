from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

site_links = []

def internal_links(linkUrl):
    html = urlopen('https://treehouse-projects.github.io/horse-land/{}'
                   .format(linkUrl))
    soup = BeautifulSoup(html, 'html.parser')

    return soup.find('a', href=re.compile('(.html)$'))

if __name__ == '__main__':
    urls = internal_links('index.html')
    while len(urls) > 0:
        if page not in site_links:
            new_page = page.attrs['href']
            print(new_page)
            site_links.append(new_page)
            urls = internal_links(new_page)
            page = urls.attrs['href']
            print(page)
            print('\n==========================\n')
            urls = internal_links(page)
        else:
            break
