import os
import json
import requests
from datetime import datetime
from src import awwwards, css_design_awards, css_winner, the_fwa

# {
#     "attachments": [
#         {
#             "color": "#f1efea",
#             "pretext": "@here Hurry and Check it!",
#             "author_name": "CSS Design Awards",
#             "author_link": "https://www.cssdesignawards.com",
#             "title": "Slack API Documentation",
#             "title_link": "https://api.slack.com/",
#             "text": "Optional text that appears within the attachment",
#             "image_url": "https://www.cssdesignawards.com/cdasites/2018/201804/20180424023416.jpg",
#             "ts": 1525874410
#         }
#     ]
# }


def main():
    if not os.path.exists('./.env'):
        print('ERROR: Not found .env!')
        return

    hashes_filename = os.getenv('HASHES_FILE', '')

    hashes = {
        'awwwards': '',
        'css_design_awards': '',
        'css_winner': '',
        'the_fwa': '',
    }

    if os.path.exists(hashes_filename):
        with open(hashes_filename, 'r') as f:
            hashes = json.loads(f.read())

    results = {
        'awwwards': awwwards.get(hashes['awwwards']),
        'css_design_awards':
        css_design_awards.get(hashes['css_design_awards']),
        'css_winner': css_winner.get(hashes['css_winner']),
        'the_fwa': the_fwa.get(hashes['the_fwa']),
    }

    attachments = []
    for key, result in results.items():
        if not bool(result):
            continue

        hashes[key] = result['current_hash']
        attachments.append({
            'ts': int(datetime.now().timestamp()),
            'color': result['color'],
            'author_name': result['author_name'],
            'author_link': result['author_link'],
            'title': result['title'],
            'title_link': result['title_link'],
            'text': result['text'],
            'image_url': result['image_url'],
        })

    if len(attachments) == 0:
        return

    slack_url = os.getenv('SLACK_WEB_HOOK_URL', '')
    requests.post(
        slack_url,
        data=json.dumps({
            'text': '<!here> Hurry and Check it!',
            'attachments': attachments
        }))
    with open(hashes_filename, 'w') as f:
        f.write(json.dumps(hashes))


if __name__ == '__main__':
    main()
