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


content = get_content('defaults/processing.html')
# content = "Processing..."
data = cgi.FieldStorage()

postid = data.getfirst('id', 0)
author = data.getfirst('author', 'Мініанус')
value = data.getfirst('value', 'Маўчыць!')

adding_post.addComment({'id': str(postid), 'value': value, 'author': author})


enc_print('Content-type: text/html\n')
enc_print(content.format(url='/cgi-bin/page.py?post=' + str(postid)))


