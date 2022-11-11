# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:45:46 2022

@author: bk19127
"""

def y_n_input(guide_text):
    while True:
        checker = input(str(guide_text))
        if checker in ["y","Y","yes","Yes"]:
            return True
            break
        elif checker in ["n","N","no","No"]:
            return False
        else:
            continue

def recreate_list_1d(target_list, add_text):
    for i in range(len(target_list)):
        temp = target_list[i]
        temp += add_text
        target_list[i] = temp