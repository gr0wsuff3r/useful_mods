# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:40:50 2022

@author: bk19127
"""

# リスト内で部分一致している要素のインデックスを返す関数
def inclusive_list_index(list_name, target_word):
    for index, list_member in enumerate(list_name):
        if target_word in list_member:
            return index
    raise IndexError