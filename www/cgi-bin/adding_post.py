import sys
import os
import json
import cgi

info = cgi.FieldStorage()

def addPost(post):
    all_posts = ''
    with open('../storage/news.json', 'r') as file_content:
        all_posts = file_content.read()
    all_posts_list = json.loads(all_posts)
    all_posts_list['news'].append(post) # post must be a dictionary
    with open('../storage/news.json', 'w') as file_to_write:
        file_to_write.write(str(all_posts_list).replace('"', '\\"'). replace("'", '"'))