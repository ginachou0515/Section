#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/2 下午 05:37
# @Author : Gina
# @Site : 
# @File : SubAuthority.py
# @Software: PyCharm

# // 判斷所屬分區
# private static String matchArea(String roadID_m, float mile) {
# 		String area = null;
# 		switch (roadID_m) {
# 		case "000010":
# 			if (mile >= 0 && mile < 100.8) {
# 				area = "NFB-NR";
# 			} else if (mile >= 100.8 && mile < 251.1) {
# 				area = "NFB-CR";
# 			} else if (mile >= 251.1 && mile < 374.32) {
# 				area = "NFB-SR";
# 			}
# 			break;
# 		case "00001A":
# 			area = "NFB-NR";
# 			break;
# 		case "00001B":
# 			area = "NFB-NR";
# 			break;
# 		case "000020":
# 			area = "NFB-NR";
# 			break;
# 		case "000030":
# 			if (mile >= 0 && mile < 110.703) {
# 				area = "NFB-NR";
# 			} else if (mile >= 110.703 && mile < 270) {
# 				area = "NFB-CR";
# 			} else if (mile >= 270 && mile < 431.525) {
# 				area = "NFB-SR";
# 			}
# 			break;
# 		case "000031":
# 			area = "NFB-NR";
# 			break;
# 		case "300026":
# 			area = "NFB-NR";
# 			break;
# 		case "626530F":
# 			area = "NFB-NR";
# 			break;
# 		case "626529F":
# 			area = "NFB-NR";
# 			break;
# 		case "000040":
# 			area = "NFB-CR";
# 			break;
# 		case "000050":
# 			area = "NFB-PL";
# 			break;
# 		case "000060":
# 			area = "NFB-CR";
# 			break;
# 		case "000080":
# 			area = "NFB-SR";
# 			break;
# 		case "000100":
# 			area = "NFB-SR";
# 			break;
# 		case "100620":
# 			area = "NFB-NR";
# 			break;
# 		case "100640":
# 			area = "NFB-NR";
# 			break;
# 		case "100660":
# 			area = "NFB-NR";
# 			break;
# 		case "100680":
# 			area = "NFB-NR";
# 			break;
# 		case "100720":
# 			area = "NFB-CR";
# 			break;
# 		case "100740":
# 			area = "NFB-CR";
# 			break;
# 		case "100741":
# 			area = "NFB-CR";
# 			break;
# 		case "100760":
# 			area = "NFB-CR";
# 			break;
# 		case "100780":
# 			area = "NFB-CR";
# 			break;
# 		case "100820":
# 			area = "NFB-SR";
# 			break;
# 		case "100840":
# 			area = "NFB-SR";
# 			break;
# 		case "100860":
# 			area = "NFB-SR";
# 			break;
# 		case "100880":
# 			area = "NFB-SR";
# 			break;
# 		default:
# 			area = "unknow";
# 		}
# 		return area;
# 	}

def freeway010(mile):
	if mile >= 0 and mile < 100.8:
		area = "NFB-NR"
	elif mile >= 100.8 and mile < 251.1:
		area = "NFB-CR"
	elif mile >= 251.1 and mile < 374.32:
		area = "NFB-SR"
	return area

def freeway01A(mile):
	area = "NFB-NR"
	return area

def freeway01B(mile):
	area = "NFB-NR"
	return area

def freeway020(mile):
	area = "NFB-NR"
	return area

def freeway030(mile):
	if mile >= 0 and mile < 110.703:
		area = "NFB-NR"
	elif mile >= 110.703 and mile < 270:
		area = "NFB-CR"
	elif mile >= 270 and mile < 431.525:
		area = "NFB-SR"
	return area

def freeway031(mile):
	area = "NFB-NR"
	return area

def primary026(mile):
	area = "NFB-NR"
	return area

def road26530F(mile):
	area = "NFB-NR"
	return area

def road26529F(mile):
	area = "NFB-NR"
	return area

def freeway040(mile):
	area = "NFB-CR"
	return area

def freeway050(mile):
	area = "NFB-PL"
	return area

def freeway060(mile):
	area = "NFB-CR"
	return area

def freeway080(mile):
	area = "NFB-SR"
	return area

def freeway100(mile):
	area = "NFB-SR"
	return area

def expressway620(mile):
	area = "NFB-NR"
	return area

def expressway640(mile):
	area = "NFB-NR"
	return area

def expressway660(mile):
	area = "NFB-NR"
	return area

def expressway680(mile):
	area = "NFB-NR"
	return area

def expressway720(mile):
	area = "NFB-CR"
	return area

def expressway740(mile):
	area = "NFB-CR"
	return area

def expressway741(mile):
	area = "NFB-CR"
	return area

def expressway760(mile):
	area = "NFB-CR"
	return area

def expressway780(mile):
	area = "NFB-CR"
	return area

def expressway820(mile):
	area = "NFB-SR"
	return area

def expressway840(mile):
	area = "NFB-SR"
	return area

def expressway860(mile):
	area = "NFB-SR"
	return area

def expressway880(mile):
	area = "NFB-SR"
	return area

def get_default():
	return 'unknow'


def notify_author(roadid, mile):
	switcher = {
		"000010": freeway010(mile),
		"00001A": freeway01A(mile),
		"00001B": freeway01B(mile),
		"000020": freeway020(mile),
		"000030": freeway030(mile),
		"000031": freeway031(mile),
		"300026": primary026(mile),
		"626530F": road26530F(mile),
		"626529F": road26529F(mile),
		"000040": freeway040(mile),
		"000050": freeway050(mile),
		"000060": freeway060(mile),
		"000080": freeway080(mile),
		"000100": freeway100(mile),
		"100620": expressway620(mile),
		"100640": expressway640(mile),
		"100660": expressway660(mile),
		"100680": expressway680(mile),
		"100720": expressway720(mile),
		"100740": expressway740(mile),
		"100741": expressway741(mile),
		"100760": expressway760(mile),
		"100780": expressway780(mile),
		"100820": expressway820(mile),
		"100840": expressway840(mile),
		"100860": expressway860(mile),
		"100880": expressway880(mile)
	}
	author = switcher.get(roadid, get_default)
	return author

result = notify_author("000010", 50)
print(result)



