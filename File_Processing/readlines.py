#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:47:40 2018

@author: ts5100551
"""

with open('file.txt', 'r') as f:
    content = f.readline()
    print(type(content))
    print(content)
    
with open('file.txt', 'r', encoding = 'UTF-8') as g:
    doc = g.readlines()
    print(doc)