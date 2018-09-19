#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:45:24 2018

@author: ts5100551
"""

f = open('file.txt', 'r')
str1 = f.read(5)
print(str1)
f.close()