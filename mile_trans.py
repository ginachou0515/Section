#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/5 上午 10:49
# @Author : Gina
# @Site : 
# @File : mile_trans.py
# @Software: PyCharm

km_str = "181K+400"
mile_str = km_str.split('K+')
km = int(mile_str[0])
m = int(mile_str[1])
mile = 1000*km + m
print(f"mile_str:{mile_str}\nkm:{km}\nm:{m}\nmile:{mile}")