#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import sys
import adding_post

err = sys.stderr


def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')


def get_content(path):
    # content = ''
    with open(path) as content_file:
        content = content_file.read()
    return content


def logger(text):
    err.write(str(text) + '\n')


content = get_content('defaults/post_added.html')

data = cgi.FieldStorage()

title = data.getfirst('title', '')
text = data.getfirst('content', '')
author = data.getfirst('tags', '')

adding_post.addPost({'id': 0, 'title': title, 'value': text, 'author': author})


enc_print('Content-type: text/html\n')
enc_print(content)


