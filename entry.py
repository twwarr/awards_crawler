import json
from src import awwwards, css_design_awards, css_winner
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

if __name__ == '__main__':
    results = [awwwards.get(), css_design_awards.get(), css_winner.get()]
    print(json.dumps(results))
