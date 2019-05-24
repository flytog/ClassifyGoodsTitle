#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@version: python3.7
@author: Jerroy Yin
@contact: 10085102@qq.com
@file: jd_corpus_segment.py
@time: 2019/5/23 16:42
@software: VS
"""
import jieba
import re


from Tools import savefile, readfile


def jd_corpus_segment(corpus_filename, seg_filename, classify_filename):
    '''
    读取原始文件train_text 里面用Tab键隔离标记
    corpus_filename = "./train_text/TraingData.txt"
    '''
    print("开始获取文件... ",corpus_filename)
    read_file = open(corpus_filename)  # 读取文件内容
    print("开始写入文件... ",seg_filename)
    seg_file = open(seg_filename,'w+') #写入目标文件
    read_line = read_file.readline()
    line_number = 0
    clasify_list = []
    clasify_count_list = []
    while read_line:
        r_str=re.split(r'\t',read_line)
        jd_line = r_str[0]
        jd_line = jd_line.encode('utf-8').strip()  # 删除空行、多余的空格
        jd_line_seg = jieba.cut(jd_line)  # 为描述内容分词
        write_line = ' '.join(jd_line_seg)
        r_str[1] = r_str[1].replace('\n','').replace('\r','')
        write_line =  r_str[1]  + '\t' + write_line + '\n'  # 将处理后的文本保存在一行
        seg_file.write(write_line)
        if  r_str[1] not in clasify_list:
            clasify_list.append(r_str[1])
            clasify_count_list.append(1)
        else:
            clasify_count_list[clasify_list.index(r_str[1])] += 1
        line_number += 1
        read_line=read_file.readline()


    read_file.close()
    seg_file.close()


    print("读取文本分词结束！！！")
    print("开始写入文件... ",classify_filename)
    classify_file = open(classify_filename,'w+') #写入分类目标文件
    for each_num in range(len(clasify_list)):
        classify_file.write(clasify_list[int(each_num)] + '\t' + str(clasify_count_list[int(each_num)]) + '\n')
    classify_file.close


if __name__ == "__main__":
    # 对训练集进行分词
    corpus_filename = "./train_text/TraingData.txt"  # 未分词分类语料库路径
    seg_filename = "./train_text/SegData.txt"  # 分词后分类语料库路径
    classify_filename = "./train_text/ClassifyData.txt"  # 分词后分类结果
    jd_corpus_segment(corpus_filename, seg_filename, classify_filename)

    # 对训练集进行分词
    corpus_filename = "./test_text/test_data.txt"  # 未分词分类语料库路径
    seg_filename = "./test_text/test_SegData.txt"  # 分词后分类语料库路径
    classify_filename = "./test_text/test_ClassifyData.txt"  # 分词后分类结果
    jd_corpus_segment(corpus_filename, seg_filename, classify_filename)
