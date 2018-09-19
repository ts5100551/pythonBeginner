#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:19:16 2018

@author: ts5100551
"""

content = '''Hello Python
中文測試
Welcome
'''

f = open('file.txt', 'w')
f.write(content)
f.close()
