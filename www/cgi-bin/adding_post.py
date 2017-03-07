# import sys
# import os
import json
import html
import markdown
# import cgi

# info = cgi.FieldStorage()


def addPost(post):
    all_posts = ''

    # POST PROCESSING

    post['title'] = html.escape(post['title'])
    post['value'] = html.escape(post['value'])
    post['author'] = html.escape(post['author'])

    post['value'] = markdown.markdown(post['value'])

    # POST ADDING

    with open('storage/news.json', 'r') as file_content:
        all_posts = file_content.read()
    all_posts_list = json.loads(all_posts)
    all_posts_list['news'].append(post)  # post must be a dictionary
    with open('storage/news.json', 'w') as file_to_write:
        file_to_write.write(str(all_posts_list).replace(
            '"', '\\"'). replace("'", '"'))

#   Format for posts:
#{
#     "id": 0, // Post id (Does not needed)
#     "title": "Пярдоліць - разам!", // Post title
#     "value": "Сябры, давайце разам дапамагаць будавацца праекту Мамка.Ме. Адпярдолім мамку разам!",
#     "author": "Вова Ўкраіне!"
#   }