#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import sys
import os
import json
import io

err = io.open('err.log', 'a', encoding='utf-8')


def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')


def get_content(path):
    content = ""
    with io.open(path, encoding='utf-8') as content_file:
        content = content_file.read()
    return content

default_content = get_content('defaults/add_page.html')

os.system('python3 adding_post.py {} {} {}'.format(title, value, author))

sys.stderr.write('Printing site...\n')
# PRINTING SITE
enc_print('Content-type: text/html\n')
enc_print(default_content.format(**value))

os.system('python3 cgi-bin/second_file.py')
err.close()