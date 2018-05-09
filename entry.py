import requests
from bs4 import BeautifulSoup
import hashlib

if __name__ == '__main__':
    response = requests.get('https://www.cssdesignawards.com')
    soup = BeautifulSoup(response.text, 'html5lib')
    parent_element = soup.find(class_='home-wotd__wrapper')
    title_element = parent_element.find(class_='home-wotd__title')
    author_element = parent_element.find(class_='home-wotd__subtitle')
    thumbnail_element = parent_element.find(
        class_='home-wotd__thumbnail').find('img')
    link_element = parent_element.find(class_='home-wotd__thumbnail').find('a')
    print(title_element.string)
    print(author_element.string)
    print(f'https://www.cssdesignawards.com/{thumbnail_element["src"]}')
    print(f'https://www.cssdesignawards.com{link_element["href"]}')
    print(hashlib.md5(response.text.encode()).hexdigest())
