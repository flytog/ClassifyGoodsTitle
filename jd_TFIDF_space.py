#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@version: python3.7
@author: Jerroy Yin
@contact: 10085102@qq.com
@file: jd_TFIDF_space.py
@time: 2019/5/23 16:42
@software: VS
"""


from sklearn.datasets.base import Bunch
from sklearn.feature_extraction.text import TfidfVectorizer
from Tools import readfile, readbunchobj, writebunchobj


def vector_space(stopword_path, bunch_path, space_path, train_tfidf_path=None):
    stpwrdlst = readfile(stopword_path).splitlines()
    bunch = readbunchobj(bunch_path)
    tfidfspace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, 
                        contents=bunch.contents, tdm=[], vocabulary={})

    if train_tfidf_path is not None:
        trainbunch = readbunchobj(train_tfidf_path)
        tfidfspace.vocabulary = trainbunch.vocabulary
        vectorizer = TfidfVectorizer(stop_words=stpwrdlst, sublinear_tf=True, max_df=0.5,
                                     vocabulary=trainbunch.vocabulary)
        tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)

    else:
        vectorizer = TfidfVectorizer(stop_words=stpwrdlst, sublinear_tf=True, max_df=0.5)
        tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
        tfidfspace.vocabulary = vectorizer.vocabulary_

    writebunchobj(space_path, tfidfspace)
    print("if-idf词向量空间实例创建成功！！！")


if __name__ == '__main__':
    stopword_path = "train_word_bag/hlt_stop_words.txt"
    bunch_path = "train_word_bag/train_set.dat"
    space_path = "train_word_bag/tfdifspace.dat"
    vector_space(stopword_path, bunch_path, space_path)

    bunch_path = "test_word_bag/test_set.dat"
    space_path = "test_word_bag/testspace.dat"
    train_tfidf_path = "train_word_bag/tfdifspace.dat"
    vector_space(stopword_path, bunch_path, space_path, train_tfidf_path)
