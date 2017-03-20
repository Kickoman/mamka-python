# import sys
import os
import json
import html
import markdown
# import cgi

# info = cgi.FieldStorage()


def addComment(comment):
    comment['id'] = int(html.escape(comment['id']))
    comment['author'] = html.escape(comment['author'])
    comment['value'] = html.escape(comment['value'])

    comment['value'] = markdown.markdown(comment['value'])

    with open('storage/comments.json', 'r') as comments_list:
        all_comments = comments_list.read()
    all_comments_list = json.loads(all_comments)

    all_comments_list['comments'][comment['id']]['comments'].append(comment)
    with open('storage/comments.json', 'w') as file_to_write:
        file_to_write.write(str(all_comments_list).replace(
            '"', '\\"').replace("'", '"'))

    # NOTIFYING
    post_link = "http://mamka.me/cgi-bin/page.py?post=" + str(comment['id'])
    os.system('python3 cgi-bin/notify.py -c' + post_link + " " + comment['author'])


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

    post_id = len(all_posts_list['news']) - 1

    # ADDING EMPTY COMMENTS FOR THIS POST

    empty_comments = {"id": 0, "comments": []}
    with open('storage/comments.json', 'r') as file_content:
        all_com = file_content.read()
    all_com_list = json.loads(all_com)
    all_com_list['comments'].append(empty_comments)
    with open('storage/comments.json', 'w') as file_to_write:
        file_to_write.write(str(all_com_list).replace(
            '"', '\\"').replace("'", '"'))

    # NOTIFYING
    post_link = "http://mamka.me/cgi-bin/page.py?post=" + str(post_id)
    os.system('python3 cgi-bin/notify.py -p' + post_link + " " + post['title'])

#   Format for posts:
#{
#     "id": 0, // Post id (Does not needed)
#     "title": "Пярдоліць - разам!", // Post title
#     "value": "Сябры, давайце разам дапамагаць будавацца праекту Мамка.Ме. Адпярдолім мамку разам!",
#     "author": "Вова Ўкраіне!"
#   }
