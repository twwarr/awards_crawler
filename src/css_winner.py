import feedparser
from bs4 import BeautifulSoup
import hashlib


def get(prev_hash=''):
    try:
        rss = feedparser.parse(
            'http://feeds.feedburner.com/csswinner?format=atom')
    except Exception as error:
        print(error)
        return

    entry = rss['entries'][0]
    current_hash = hashlib.md5(entry['summary'].encode()).hexdigest()
    if prev_hash == current_hash:
        return

    soup = BeautifulSoup(entry['summary'], 'html5lib')

    return {
        'current_hash': current_hash,
        'color': '#e45151',
        'author_name': 'CSS Winner',
        'author_link': 'http://www.csswinner.com/',
        'title': entry['title'],
        'title_link': entry['link'],
        'text': '(UNKNOWN)',
        'image_url': soup.find('img')['src']
    }
