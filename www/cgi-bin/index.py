#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import sys
import os
import json
import get_post

err = open('err.log', 'a')
err = sys.stderr


def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')


def get_content(path):
    content = ""
    with open(path) as content_file:
        content = content_file.read()
    return content

default_content = get_content('/defaults/default_content.html')
article = get_content('/defaults/article.html')

info = cgi.FieldStorage()
current_page = info.getfirst('page', 1)

toformat = get_post.getPage(current_page)

news_list = ""

for i in toformat:
    current_post = article.format(**i)
    news_list = current_post + news_list

sys.stderr.write('Printing site...\n')

err.write('\n\n\n' + get_post.computePages(int(current_page)) + '\n\n\n')
### PRINTING SITE
enc_print('Content-type: text/html\n')
enc_print(default_content.format(news_list, pages=get_post.computePages(current_page)))

os.system('python3 cgi-bin/second_file.py')
err.close()
