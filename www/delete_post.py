# import os
import sys
import json


post_id = int(sys.argv[1])

with open('storage/news.json', 'r') as file_content:
    all_posts = file_content.read()
all_posts_list = json.loads(all_posts)

new_posts_list = all_posts_list
del(new_posts_list['news'][post_id])


with open('storage/news.json', 'w') as file_to_write:
    file_to_write.write(str(new_posts_list).replace(
        '"', '\\"'). replace("'", '"'))


with open('storage/comments.json', 'r') as file_content:
    all_com = file_content.read()

all_com_list = json.loads(all_com)
new_com_list = all_com_list
del(new_com_list['comments'][post_id])

with open('storage/comments.json', 'w') as file_to_write:
    file_to_write.write(str(new_com_list).replace(
        '"', '\\"').replace("'", '"'))
