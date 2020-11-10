#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/2 下午 05:37
# @Author : Gina
# @Site :
# @File : SubAuthority.py
# @Software: PyCharm


def freeway010(mile):
    if mile >= 0 and mile < 100800: ###110.703公里  110703公尺
        return "NFB-NR"
    elif mile >= 100800 and mile < 251100:
        return "NFB-CR"
    elif mile >= 251100: ##and mile < 374320 最尾端可以先刪除
        return "NFB-SR"


def freeway01A(mile):
    return "NFB-NR"


def freeway01B(mile):
    return "NFB-NR"


def freeway020(mile):
    return "NFB-NR"


def freeway030(mile):
    if mile >= 0 and mile < 110703:  ###110.703公里  110703公尺
        return "NFB-NR"
    elif mile >= 110703 and mile < 270000:
        return "NFB-CR"
    elif mile >= 270000:  ## and mile < 431525
        return "NFB-SR"


def freeway031(mile):
    return "NFB-NR"


def primary026(mile):
    return "NFB-NR"


def road26530F(mile):
    return "NFB-NR"


def road26529F(mile):
    return "NFB-NR"


def freeway040(mile):
    return "NFB-CR"


def freeway050(mile):
    return "NFB-PL"


def freeway060(mile):
    return "NFB-CR"


def freeway080(mile):
    return "NFB-SR"


def freeway100(mile):
    return "NFB-SR"


def expressway620(mile):
    return "NFB-NR"


def expressway640(mile):
    return "NFB-NR"


def expressway660(mile):
    return "NFB-NR"


def expressway680(mile):
    return "NFB-NR"


def expressway720(mile):
    return "NFB-CR"


def expressway740(mile):
    return "NFB-CR"


def expressway741(mile):
    return "NFB-CR"


def expressway760(mile):
    return "NFB-CR"


def expressway780(mile):
    return "NFB-CR"


def expressway820(mile):
    return "NFB-SR"


def expressway840(mile):
    return "NFB-SR"


def expressway860(mile):
    return "NFB-SR"


def expressway880(mile):
    return "NFB-SR"


def get_default(mile):
    return "unknow"


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
        "100880": expressway880(mile),
    }
    author = switcher.get(roadid, get_default(mile))
    return author


if __name__ == "__main__":
    result = notify_author("000010", 50)
    print(result)
    result2 = notify_author("000030", 300)
    print(result2)
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
