import requests
from bs4 import BeautifulSoup
import hashlib
import json


def get(prev_hash=''):
    try:
        response = requests.get('https://www.awwwards.com/websites/')
    except Exception as error:
        print(error)
        return

    current_hash = hashlib.md5(response.text.encode()).hexdigest()
    if prev_hash == current_hash:
        return

    soup = BeautifulSoup(response.text, 'html5lib')
    parent_element = soup.find(class_='js-collectable')
    data = json.loads(parent_element["data-model"])
    info_element = parent_element.find(class_='box-info')
    author_element = info_element.find(class_='by').find('strong')
    link_element = info_element.find(class_='content').find('a')

    return {
        'current_hash':
        current_hash,
        'color':
        '#49c5b6',
        'author_name':
        'Awwwards',
        'author_link':
        'https://www.awwwards.com',
        'title':
        data['title'],
        'title_link':
        f'https://www.awwwards.com{link_element["href"]}',
        'text':
        author_element.string,
        'image_url':
        f'https://assets.awwwards.com/awards/media/cache/thumb_417_299/{data["images"]["thumbnail"]}'
    }
