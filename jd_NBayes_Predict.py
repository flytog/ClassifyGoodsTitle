#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@version: python3.7
@author: Jerroy Yin
@contact: 10085102@qq.com
@file: jd_NBayes_Predict.py
@time: 2019/5/23 16:42
@software: VS
"""


from sklearn.naive_bayes import MultinomialNB  # 导入多项式贝叶斯算法
from sklearn import metrics
from Tools import readbunchobj

# 导入训练集
trainpath = "train_word_bag/tfdifspace.dat"
train_set = readbunchobj(trainpath)

# 导入测试集
testpath = "test_word_bag/testspace.dat"
test_set = readbunchobj(testpath)

# 训练分类器：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高
clf = MultinomialNB(alpha=0.000001).fit(train_set.tdm, train_set.label)

# 预测分类结果
predicted = clf.predict(test_set.tdm)

for content, file_name, expct_cate in zip(test_set.contents, test_set.filenames, predicted):
#    if flabel != expct_cate:
     print(file_name, " -->预测类别:", expct_cate, ": 实际内容:", content)

print("预测完毕!!!")

# 计算分类精度：

def metrics_result(actual, predict):
    print('精度:{0:.3f}'.format(metrics.precision_score(actual, predict, average='weighted')))
    print('召回:{0:0.3f}'.format(metrics.recall_score(actual, predict, average='weighted')))
    print('f1-score:{0:.3f}'.format(metrics.f1_score(actual, predict, average='weighted')))


metrics_result(test_set.label, predicted)
