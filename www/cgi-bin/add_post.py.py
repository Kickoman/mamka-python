#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import sys
import os
import json

err = open('err.log', 'a')

def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')

def get_content(path):
    content = ""
    with open(path) as content_file:
        content = content_file.read()
    return content

default_content = get_content('../defaults/add_page.html')


value = {"value" : news_dict[i]['value'], "author" : news_dict[i]['author'],
         "title" : news_dict[i]['title']}

sys.stderr.write('Printing site...\n')
### PRINTING SITE
enc_print('Content-type: text/html\n')
enc_print(default_content.format(**value))

os.system('python3 cgi-bin/second_file.py')
err.close()