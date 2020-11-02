#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/2 下午 05:37
# @Author : Gina
# @Site : 
# @File : SubAuthority.py
# @Software: PyCharm

# // 判斷所屬分區
# private
# static
# String
# matchArea(String
# roadID_m, float
# mile) {
#     String
# area = null;
# switch(roadID_m)
# {
#     case
# "000010":
# if (mile >= 0 & & mile < 100.8) {
# area = "NFB-NR";
# } else if (mile >= 100.8 & & mile < 251.1) {
# area = "NFB-CR";
# } else if (mile >= 251.1 & & mile < 374.32) {
# area = "NFB-SR";
# }
# break;
# case
# "00001A":
# area = "NFB-NR";
# break;
# case
# "00001B":
# area = "NFB-NR";
# break;
# case
# "000020":
# area = "NFB-NR";
# break;
# case
# "000030":
# if (mile >= 0 & & mile < 110.703) {
# area = "NFB-NR";
# } else if (mile >= 110.703 & & mile < 270) {
# area = "NFB-CR";
# } else if (mile >= 270 & & mile < 431.525) {
# area = "NFB-SR";
# }
# break;
# case
# "000031":
# area = "NFB-NR";
# break;
# case
# "300026":
# area = "NFB-NR";
# break;
# case
# "626530F":
# area = "NFB-NR";
# break;
# case
# "626529F":
# area = "NFB-NR";
# break;
# case
# "000040":
# area = "NFB-CR";
# break;
# case
# "000050":
# area = "NFB-PL";
# break;
# case
# "000060":
# area = "NFB-CR";
# break;
# case
# "000080":
# area = "NFB-SR";
# break;
# case
# "000100":
# area = "NFB-SR";
# break;
# case
# "100620":
# area = "NFB-NR";
# break;
# case
# "100640":
# area = "NFB-NR";
# break;
# case
# "100660":
# area = "NFB-NR";
# break;
# case
# "100680":
# area = "NFB-NR";
# break;
# case
# "100720":
# area = "NFB-CR";
# break;
# case
# "100740":
# area = "NFB-CR";
# break;
# case
# "100741":
# area = "NFB-CR";
# break;
# case
# "100760":
# area = "NFB-CR";
# break;
# case
# "100780":
# area = "NFB-CR";
# break;
# case
# "100820":
# area = "NFB-SR";
# break;
# case
# "100840":
# area = "NFB-SR";
# break;
# case
# "100860":
# area = "NFB-SR";
# break;
# case
# "100880":
# area = "NFB-SR";
# break;
# default:
# area = "unknow";
# }
# return area;
# }