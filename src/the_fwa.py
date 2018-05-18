import re
import requests
from bs4 import BeautifulSoup
import hashlib
import json
import subprocess


def get(prev_hash=''):
    try:
        response = requests.get('https://thefwa.com/awards')
    except Exception as error:
        print(error)
        return

    soup = BeautifulSoup(response.text, 'html5lib')
    js_code = soup.find('script').text.strip()
    remove_comment_code = re.sub('<!--.+-->', '', js_code)
    node_response = subprocess.run(
        [
            'node', '-e',
            f'{remove_comment_code} console.log(JSON.stringify(konfig))'
        ],
        stdout=subprocess.PIPE)
    info = json.loads(node_response.stdout)

    current_hash = hashlib.md5(
        info['caseMenu'][0]['item']['title'].encode()).hexdigest()
    if prev_hash == current_hash:
        return

    return {
        'current_hash':
        current_hash,
        'color':
        '#ffca00',
        'author_name':
        'The FWA',
        'author_link':
        'https://thefwa.com',
        'title':
        info['caseMenu'][0]['item']['title'],
        'title_link':
        f'https://thefwa.com/cases/{info["caseMenu"][0]["item"]["slug"]}',
        'text':
        '(UNKNOWN)',
        'image_url':
        f'https://thefwa.com{info["caseMenu"][0]["item"]["slide1"]["538"]["span10"]}'
    }
