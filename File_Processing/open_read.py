#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:21:46 2018

@author: ts5100551
"""

f = open('file.txt', 'r')
for line in f:
    print(line, end="")
f.close()