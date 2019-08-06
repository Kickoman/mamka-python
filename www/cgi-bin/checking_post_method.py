
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import sys


def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')


data = cgi.FieldStorage()

text = data.getfirst('content', 'fuck')

enc_print('Content type: text/html\n')
enc_print('{}'.format(str(text)))
