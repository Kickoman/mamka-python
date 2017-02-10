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

catalog = get_content('storage/news.json')
catalog_dict = json.loads(catalog)

def getPost(x):
    post = catalog_dict['news'][x]
    res = {'postid' : post['id'],
           'title' : post['title'],
           'value' : post['value'],
           'author' : post['author']}
    return res

def getPage(page):
    page = int(page)
    last = len(catalog_dict['news']) - 10 * (page - 1) - 1
    posts = []
    for i in range(min(10, last + 1)):
        post = getPost(last - i)
        posts.append(post)
    posts.reverse()
    err.write('\n\n\n' + str(posts) + '\n\n\n')
    return posts

def computePages(currentPage):
    currentPage = int(currentPage)
    all_pages = len(catalog_dict['news']) // 10 + (1 if len(catalog_dict['news']) % 10 != 0 else 0)
    page_bar = get_content('../defaults/pages_bar.html')

    # result = {'before' : "", 'current' : "", 'after' : ""}
    result = {}

    result['current'] = str(currentPage)

    if (currentPage == 1):
        result['before'] = ""
    elif (currentPage == 2):
        result['before'] = '<a href="index.py?page=1" class="pagebar">1</a>'
    elif currentPage == 3:
        result['before'] = '<a href="index.py?page=1" class="pagebar">1</a> <a href="index.py?page=2" class="pagebar">2</a>'
    else:
        result['before'] = '<a href="index.py?page=1" class="pagebar">1</a> ... <a href="index.py?page=' +\
                            str(currentPage - 1) + '" class="pagebar">' + str(currentPage - 1) + '</a>'

    if (currentPage == all_pages):
        result['after'] = ""
        # sys.stderr.write('OLOLO\n\n')
    elif currentPage == all_pages - 1:
        result['after'] = '<a href="index.py?page=' + str(all_pages) + '" class="pagebar">' +\
                           str(all_pages) + '</a>'
    elif currentPage == all_pages - 2:
        result['after'] = '<a href="index.py?page=' + str(all_pages - 1) + '" class="pagebar">' +\
                           str(all_pages - 1) + '</a> <a href="index.py?page=' + str(all_pages) + '" class="pagebar">' +\
                           str(all_pages) + '</a>'
    else:
        result['after'] = '<a href="index.py?page=' + str(currentPage + 1) + '" class="pagebar">' + str(currentPage + 1) + '</a>' +\
                          '... <a href="index.py?page=' + str(all_pages) + '" class="pagebar">' + str(all_pages) + '</a>'

    return page_bar.format(**result)