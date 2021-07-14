import csv
import jieba as jieba
import re
import pandas as pd
#读取文件，文件读取函数
def read_file(filename):
    with  open(filename, 'r',encoding='utf-8')as f:
        text = f.read()
        #返回list类型数据
        text = text.split('\n')
    return text
#将数据写入文件中
def write_data(filename,data):
    with open(filename,'a',encoding='utf-8')as f:
        f.write(str(data))
#去停用词
def del_stopwords(words):
    stopwords = read_file(r"")# 读取停用词表
    # 去除停用词后的句子
    new_words = []
    for word in words:
        if word not in stopwords:
            new_words.append(word)
    return new_words