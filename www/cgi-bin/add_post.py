#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import json
import sys
import adding_post


def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')


def get_content(path):
    content = ''
    with open(path) as content_file:
        content = content_file.read()
    return content


def logger(text):
    err.write(str(text) + '\n')


content = get_content('/defaults/add_page.html')

info = cgi.FieldStorage()
value = info.getfirst('content', 'fuck')
title = info.getfirst('title', 'fuck')
author = info.getfirst('tags', 'fuck')


enc_print('Content-type: text/html\n')
enc_print('{} {} {}\n'.format(title, value, author))

#enc_print(content)

