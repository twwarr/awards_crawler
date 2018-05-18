import requests
from bs4 import BeautifulSoup
import hashlib


def get(prev_hash=''):
    try:
        response = requests.get('https://www.cssdesignawards.com')
    except Exception as error:
        print(error)
        return

    soup = BeautifulSoup(response.text, 'html5lib')
    parent_element = soup.find(class_='home-wotd__wrapper')
    title_element = parent_element.find(class_='home-wotd__title')
    author_element = parent_element.find(class_='home-wotd__subtitle')
    thumbnail_element = parent_element.find(
        class_='home-wotd__thumbnail').find('img')
    link_element = parent_element.find(class_='home-wotd__thumbnail').find('a')

    current_hash = hashlib.md5(title_element.string.encode()).hexdigest()
    if prev_hash == current_hash:
        return

    return {
        'current_hash': current_hash,
        'color': '#f1efea',
        'author_name': 'CSS Design Awards',
        'author_link': 'https://www.cssdesignawards.com',
        'title': title_element.string,
        'title_link': f'https://www.cssdesignawards.com{link_element["href"]}',
        'text': author_element.string,
        'image_url':
        f'https://www.cssdesignawards.com/{thumbnail_element["src"]}'
    }
