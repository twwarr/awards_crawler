import requests
from bs4 import BeautifulSoup
import hashlib
import json


def get(prev_hash=''):
    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36'
        }
        response = requests.get(
            'https://www.awwwards.com/websites/', headers=headers)
    except Exception as error:
        print(error)
        return

    soup = BeautifulSoup(response.text, 'html5lib')
    parent_element = soup.find(class_='js-collectable')
    data = json.loads(parent_element["data-model"])
    info_element = parent_element.find(class_='box-info')
    author_element = info_element.find(class_='by').find('strong')
    link_element = info_element.find(class_='content').find('a')

    current_hash = hashlib.md5(data['title'].encode()).hexdigest()
    if prev_hash == current_hash:
        return

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


if __name__ == '__main__':
    print(get())
