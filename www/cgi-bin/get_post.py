#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import io

err = io.open('err.log', 'a', encoding='utf-8')
err = sys.stderr


def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')


def get_content(path):
    content = ""
    with io.open(path, 'r', encoding='utf-8') as content_file:
        content = content_file.read()
    return content

catalog = get_content('storage/news.json')
catalog_dict = json.loads(catalog)

comments = get_content('storage/comments.json')
comments_dict = json.loads(comments)


def getPostComments(x):
    x = int(x)
    cur_comments = comments_dict['comments'][x]
    comment_block = get_content('defaults/comment_block.html')
    result = ""
    for i in cur_comments['comments']:
        cur_block = comment_block.format(**i)
        result += cur_block
    if result == "":
        result = "<p>Камэнтароў няма! Вы хто такія?</p>"
    return result


def getPost(x):
    post = catalog_dict['news'][x]
    res = {'postid' : x,
           'title' : post['title'],
           'value' : post['value'],
           'author' : post['author'],
           'comments' : getPostComments(x)}
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
    page_bar = get_content('defaults/pages_bar.html')

    result = {}

    result['current'] = '<a class="btm-page selected">' + str(currentPage) + '</a>'

    if currentPage == 1:
        result['before'] = ""
    elif currentPage == 2:
        result['before'] = '<a href="index.py?page=1" class="btm-page">1</a>'
    elif currentPage == 3:
        result['before'] = '<a href="index.py?page=1" class="btm-page">1</a> <a href="index.py?page=2" class="btm-page">2</a>'
    else:
        result['before'] = '<a href="index.py?page=1" class="btm-page">1</a> <div class="btm-dots">...</div> <a href="index.py?page=' +\
                            str(currentPage - 1) + '" class="btm-page">' + str(currentPage - 1) + '</a>'

    if currentPage == all_pages:
        result['after'] = ""
    elif currentPage == all_pages - 1:
        result['after'] = '<a href="index.py?page=' + str(all_pages) + '" class="btm-page">' +\
                           str(all_pages) + '</a>'
    elif currentPage == all_pages - 2:
        result['after'] = '<a href="index.py?page=' + str(all_pages - 1) + '" class="btm-page">' +\
                           str(all_pages - 1) + '</a> <a href="index.py?page=' + str(all_pages) + '" class="btm-page">' +\
                           str(all_pages) + '</a>'
    else:
        result['after'] = '<a href="index.py?page=' + str(currentPage + 1) + '" class="btm-page">' + str(currentPage + 1) + '</a>' +\
                          '<div class="btm-dots">...</div> <a href="index.py?page=' + str(all_pages) + '" class="btm-page">' + str(all_pages) + '</a>'

    return page_bar.format(**result)
