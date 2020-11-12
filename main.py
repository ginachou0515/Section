#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/12 上午 09:46
# @Author : Gina
# @Site : 
# @File : main.py
# @Software: PyCharm

import xml.etree.ElementTree as ET
import os
import pandas as pd
import datetime
import SubAuthority
import section_revise
import section_road_author


if __name__ == "__main__":
    path = os.getcwd()
    DIR_ROOT = os.path.join(path)
    xml_name = "Section.xml"
    if not os.path.exists(DIR_ROOT):
        os.makedirs(DIR_ROOT)
    file_name = os.path.join(DIR_ROOT, xml_name)

    section_revise.section_road_find_author(path, xml_name, file_name)

    xml_name2 = "SectionLinkList.xml"
    section_road_author.section_find_author(path, xml_name2)

    xml_name3 = "SectionShapeList.xml"
    section_road_author.section_find_author(path, xml_name3)