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
import datetime
import SubAuthority


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
    mile_str = km_str.split("K+")
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

    """
    創建命名空間後，後面創建節點的時候，定義節點標籤，和定義節點標籤屬性的時候，在裡面加入命名名稱值 如【"{命名名稱值}節點標籤名稱"】，這樣會自動將命名名稱值轉換成命名名稱
    簡單的理解就是，給標籤，標籤屬性，加上一個標示，防止名稱衝突
    """
    ET.register_namespace("", "http://ptx.transportdata.tw/standard/schema/TIX")
    ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")
    ET.register_namespace(
        "schemaLocation", "http://ptx.transportdata.tw/standard/schema"
    )
    ns = {"List": "http://ptx.transportdata.tw/standard/schema/TIX",
          "xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "schemaLocation": "http://ptx.transportdata.tw/standard/schema"}

    col_db = [
        "db_key",
        "section_id",
        "author",
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

        for mile in element.findall(".//List:SectionMile", ns):
            StartKM = mile.find(".//List:StartKM", ns)
            EndKM = mile.find(".//List:EndKM", ns)

            start_mile = StartKM.text
            start_mile = str_trans_mile(start_mile)
            end_mile = EndKM.text
            end_mile = str_trans_mile(end_mile)
            print(f"起始里程:{start_mile}\n結束里程:{end_mile}")

        try:
            author = SubAuthority.notify_author(road_id, start_mile)
            print(f"所屬單位:{author}")
        except:
            print("未知異常")

        section_list = [(db_key, section_id, author, road_id, time, start_mile, end_mile)]
        section_new = pd.DataFrame(section_list, columns=col_db)
        section_db = section_db.append(section_new, ignore_index=True)
        section_db["section_id"] = section_db["section_id"].astype(str)
        section_db["road_id"] = section_db["road_id"].astype(str)


        # Element(標籤名):創建標籤節點對象
        new_node = ET.Element("SubAuthorityCode")
        # 添加標籤值
        new_node.text = author
        print(f"添加標籤值:{author}")
        # insert(index, element):在指定位置插入子元素。
        element.insert(1, new_node)

        # 添加標籤　直接增加在最末端
        # element.append(new_node)
        # """
        # 創建命名空間後，後面創建節點的時候，定義節點標籤，和定義節點標籤屬性的時候，在裡面加入命名名稱值 如【"{命名名稱值}節點標籤名稱"】，這樣會自動將命名名稱值轉換成命名名稱
        # 簡單的理解就是，給標籤，標籤屬性，加上一個標示，防止名稱衝突
        # """
        # ET.register_namespace("", "http://ptx.transportdata.tw/standard/schema/TIX")
        # ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")
        # ET.register_namespace(
        #     "schemaLocation", "http://ptx.transportdata.tw/standard/schema"
        # )
        # 回寫xml數據
        tree.write("NewSection.xml", encoding="utf-8", xml_declaration=True)
        print(f"新增後XML:{tree}")

    print(f"最終新增的XML:{tree}")
    print(f"解析結果:{section_db}")

##無法解開啟EXCEL時，將section_id和road_id以數值類型讀取
    output_name = "ReviseSection.xlsx"
    outputpath = os.path.join(path, output_name)
    section_db.to_excel(outputpath, index=False)
