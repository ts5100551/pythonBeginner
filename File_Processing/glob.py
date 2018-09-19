#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:43:19 2018

@author: ts5100551
"""

import glob
files = glob.glob("glob.py") + glob.glob("os*.py")
for file in files:
    print(file)