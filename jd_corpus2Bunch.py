#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@version: python3.7
@author: Jerroy Yin
@contact: 10085102@qq.com
@file: jd_corpus2Bunch.py
@time: 2019/5/23 16:42
@software: VS
"""

import os
import pickle
import re

from sklearn.datasets.base import Bunch
from Tools import readfile


def jd_corpus2Bunch(wordbag_path, seg_filename, classify_filename):
    print("打开分类目录文件...",classify_filename)
    clasify_list = []
    classify_file = open(classify_filename,'r')
    read_line = classify_file.readline()
    while read_line:
        clasify_list.append(re.split(r'\t',read_line)[0]) # 获取文件中的分类信息
        read_line = classify_file.readline()
    classify_file.close
    print("关闭分类目录文件...",classify_filename)

    # 创建一个Bunch实例
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(clasify_list)
    '''
    extend(addlist)是python list中的函数，意思是用新的list（addlist）去扩充
    原来的list
    '''
    print("打开训练文件...",seg_filename)

    seg_file = open(seg_filename,'r')
    read_line = seg_file.readline()
    Line_Count = 0
    while read_line:
        r_str=re.split(r'\t',read_line)
        r_str[1] = r_str[1].replace('\n','').replace('\r','')
        bunch.label.append(r_str[0])
        bunch.filenames.append(Line_Count)
        bunch.contents.append(r_str[1])  # 读取每一行分类内容
        Line_Count += 1
        read_line = seg_file.readline()

    seg_file.close()
    # 将bunch存储到wordbag_path路径中
    with open(wordbag_path, "wb+") as file_obj:
        pickle.dump(bunch, file_obj)
    file_obj.close
    print("构建文本对象结束！！！")


if __name__ == "__main__":
    # 对训练集进行Bunch化操作：
    wordbag_path = "./train_word_bag/train_set.dat"  # Bunch存储路径
    seg_filename = "./train_text/SegData.txt"  # 分词后分类语料库路径
    classify_filename = "./train_text/ClassifyData.txt"  # 分词后分类结果
    jd_corpus2Bunch(wordbag_path, seg_filename, classify_filename)

    # 对训练集进行Bunch化操作：
    wordbag_path = "./test_word_bag/test_set.dat"  # Bunch存储路径
    seg_filename = "./test_text/test_SegData.txt"  # 分词后分类语料库路径
    classify_filename = "./test_text/test_ClassifyData.txt"  # 分词后分类结果
    jd_corpus2Bunch(wordbag_path, seg_filename, classify_filename)

