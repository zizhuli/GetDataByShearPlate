#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Date : 2023/3/1 11:50
# @Author : HELIN
import pandas as pd


"""

将txt文件内容转换为csv

"""

df = pd.read_csv("传输内容.txt", sep='\t')
print(df)
df.to_csv('传输内容.csv', encoding='utf-8-sig', index=False)
