#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/5 上午 09:09
# @Author : Gina
# @Site : 
# @File : section_revise.py
# @Software: PyCharm

import xml.etree.ElementTree as ET
import os
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP
import datetime
import time
import SubAuthority

"""
:param path:目前所在路徑/motc20/type(section)
:param date:日期名稱(str) %Y%m%d
:param date:時間段(str) %H%M
:param xml_name:xml檔案名稱
:return section_db:vd處理過後的 dataframe資料
"""
def str_trans_time(time_input, form):
    """
    :param time_input:文字格式的輸入時間
    :param form:文字格式代表的時間  EX:"%Y-%m-%d %H:%M:%S"  "%H%M"
    :return time_datetime:時間格式
    """
    time_datetime = datetime.datetime.strptime(time_input, form)  ##文字轉時間格式
    return time_datetime

def time_trans_str(time_input, form):
    """
    :param time_input:輸入時間
    :param form:時間格式轉文字後,輸出的文字格式  EX:"%Y-%m-%d %H:%M:%S"  "%H%M"
    :return time_str:輸出的文字
    """
    time_str = time_input.strftime(form)  ##文字轉時間格式
    return time_str

def str_trans_mile(km_str):
    """
    :param km_str:里程(字元) XXXK+XXX
    :return mile:運算後的里程數(INT)
    """
    mile_str = km_str.split('K+')
    km = int(mile_str[0])
    m = int(mile_str[1])
    mile = 1000 * km + m
    return mile

if __name__ == "__main__":
    path = os.getcwd()
    DIR_ROOT = os.path.join(path)
    xml_name = "Section.xml"
    if not os.path.exists(DIR_ROOT):
        os.makedirs(DIR_ROOT)
    file_name = os.path.join(DIR_ROOT, xml_name)

    tree = ET.parse(file_name)
    root = tree.getroot()
    print(root)

#http://ptx.transportdata.tw/standard/schema/TIX
#http://traffic.transportdata.tw/standard/traffic/schema/
    ns = {"List": "http://ptx.transportdata.tw/standard/schema/TIX"}
    ##http://ptx.transportdata.tw/standard/schema/
    col_db = [
        "db_key",
        "section_id",
        "road_id",
        "time",
        "start_mile",
        "end_mile",
    ]
    section_db = pd.DataFrame(columns=col_db)

    UpdateTime = root.find("List:UpdateTime", ns)
    print(f"更新時間:{UpdateTime}")
    for element in root.findall("List:Sections/List:Section", ns):
        tag = element.tag  # 訪問Element標籤
        # 獲取路段
        SectionID = element.find("List:SectionID", ns)
        RoadID = element.find("List:RoadID", ns)

        isoStr = UpdateTime.text
        time = datetime.datetime.strptime(isoStr, "%Y-%m-%dT%H:%M:%S+08:00")

        section_id = SectionID.text
        road_id = RoadID.text
        db_key = section_id + "_" + time_trans_str(time, "%Y-%m-%d %H:%M:%S")

        print(f"上傳時間:{time}\n路段ID:{section_id}\n道路ID:{road_id}")

        # 用來儲存一個路段的的里程資料
        # section_startKM = []  ##起始里程 []
        for mile in element.findall(".//List:SectionMile", ns):
            StartKM = mile.find(".//List:StartKM", ns)
            EndKM = mile.find(".//List:EndKM", ns)

            start_mile = StartKM.text
            start_mile = str_trans_mile(start_mile)
            end_mile = EndKM.text
            end_mile = str_trans_mile(end_mile)
            print(f"起始里程:{start_mile}\n結束里程:{end_mile}")
            # section_startKM += [
            #     start_mile
            # ]  # extend()方法 多項資料加在原來資料的最後，但是必須把這些資料放在一個List資料組

        section_list = [
            (
                db_key,
                section_id,
                road_id,
                time,
                start_mile,
                end_mile,
            )
        ]

        author = SubAuthority.notify_author(road_id, start_mile)
        print(f"所屬單位:{author}")
        section_new = pd.DataFrame(section_list, columns=col_db)
        section_db = section_db.append(section_new, ignore_index=True)
    print(f"解析結果:{section_db}")


