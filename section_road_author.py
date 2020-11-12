#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/10 下午 03:12
# @Author : Gina
# @Site : 
# @File : section_road_author.py
# @Software: PyCharm

import xml.etree.ElementTree as ET
import os
import pandas as pd
import datetime

def time_trans_str(time_input, form):
    """
    :param time_input:輸入時間
    :param form:時間格式轉文字後,輸出的文字格式  EX:"%Y-%m-%d %H:%M:%S"  "%H%M"
    :return time_str:輸出的文字
    """
    time_str = time_input.strftime(form)  ##文字轉時間格式
    return time_str


def section_find_author(path, xml_name):
    """
    :param path:所有檔案路徑
    :param xml_name:讀入的XML檔名稱

    :return 輸出XML檔
    """

    DIR_ROOT = os.path.join(path)
    if not os.path.exists(DIR_ROOT):
        os.makedirs(DIR_ROOT)
    file_name = os.path.join(DIR_ROOT, xml_name)
    tree = ET.parse(file_name)
    root = tree.getroot()

##讀取Section根據RoadId判斷的所屬機關輸出檔
    DIR_ROOT = os.path.join(path)
    section_revise = "ReviseSection.xlsx"
    file_revise = os.path.join(DIR_ROOT, section_revise)
    ##讀取資料時，先把section_id和road_id類型定為str
    section_df = pd.read_excel(file_revise, dtype={'section_id':str, 'road_id':str})

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
        "section_id",
        "time",
        "author",
    ]
    SectionLinkList_db = pd.DataFrame(columns=col_db)

    tag = xml_name.split('List')[0]
    UpdateTime = root.find("List:UpdateTime", ns)
    for element in root.findall(f"List:{tag}s/List:{tag}", ns):
        # 獲取路段
        SectionID = element.find("List:SectionID", ns)
        section_id = SectionID.text
        isoStr = UpdateTime.text
        time = datetime.datetime.strptime(isoStr, "%Y-%m-%dT%H:%M:%S+08:00")
        # df_sel = section_df[section_df.section_id == section_id]    ##dataframe
        authority = section_df.loc[section_df.section_id == section_id, "author"].values[0]

        # db_key = section_id + "_" + time_trans_str(time, "%Y-%m-%d %H:%M:%S")
        print(f"上傳時間:{time}\n路段ID:{section_id}\n所屬機關:{authority}")
        section_list = [(section_id, time, authority)]
        section_new = pd.DataFrame(section_list, columns=col_db)
        SectionLinkList_db = SectionLinkList_db.append(section_new, ignore_index=True)

        # Element(標籤名):創建標籤節點對象
        new_node = ET.Element("SubAuthorityCode")
        # 添加標籤值
        new_node.text = authority
        # insert(index, element):在指定位置插入子元素。
        element.insert(1, new_node)

        # 回寫xml數據
        tree.write(f"New{xml_name}", encoding="utf-8", xml_declaration=True)

    print(f"{xml_name}解析結果\n:{SectionLinkList_db}")


if __name__ == "__main__":
    path = os.getcwd()
    DIR_ROOT = os.path.join(path)
    # xml_name = "SectionLinkList.xml"
    xml_name = "SectionShapeList.xml"
    if not os.path.exists(DIR_ROOT):
        os.makedirs(DIR_ROOT)
    file_name = os.path.join(DIR_ROOT, xml_name)

    ##DEF內文
    tree = ET.parse(file_name)
    root = tree.getroot()
    ##讀取Section根據RoadId判斷的所屬機關輸出檔
    section_revise = "ReviseSection.xlsx"
    file_revise = os.path.join(DIR_ROOT, section_revise)
    ##讀取資料時，先把section_id和road_id類型定為str
    section_df = pd.read_excel(file_revise, dtype={'section_id':str, 'road_id':str})

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
        "time",
        "author",
    ]
    SectionLinkList_db = pd.DataFrame(columns=col_db)

    UpdateTime = root.find("List:UpdateTime", ns)
    for element in root.findall("List:SectionLinks/List:SectionLink", ns):
        # 獲取路段
        SectionID = element.find("List:SectionID", ns)
        section_id = SectionID.text
        isoStr = UpdateTime.text
        time = datetime.datetime.strptime(isoStr, "%Y-%m-%dT%H:%M:%S+08:00")
        # df_sel = section_df[section_df.section_id == section_id]  ##dataframe
        authority = section_df.loc[section_df.section_id == section_id, "author"].values[0]

        db_key = section_id + "_" + time_trans_str(time, "%Y-%m-%d %H:%M:%S")
        print(f"上傳時間:{time}\n路段ID:{section_id}\n所屬機關:{authority}")
        section_list = [(db_key, section_id, time, authority)]
        section_new = pd.DataFrame(section_list, columns=col_db)
        SectionLinkList_db = SectionLinkList_db.append(section_new, ignore_index=True)

        # Element(標籤名):創建標籤節點對象
        new_node = ET.Element("SubAuthorityCode")
        # 添加標籤值
        new_node.text = authority
        # insert(index, element):在指定位置插入子元素。
        element.insert(1, new_node)

        # 回寫xml數據
        tree.write(f"New{xml_name}", encoding="utf-8", xml_declaration=True)
        # print(f"新增後XML:{tree}")

    print(f"解析結果:{SectionLinkList_db}")