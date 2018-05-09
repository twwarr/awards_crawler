import json
from src import css_design_awards
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
    css_design_awards_result = css_design_awards.get()
    print(json.dumps(css_design_awards_result))
