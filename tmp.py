#!/usr/bin/env python
# -*- coding:UTF-8 -*-
__author__ = '217小月月坑'
'''
BS4删除三兄弟对比
'''

from bs4 import BeautifulSoup
# clear() 方法移除当前tag的内容:
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_clear = soup.a
i_clear = soup.i.clear()
# extract() 方法将当前tag移除文档树,并作为方法结果返回
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_extract = soup.a
i_extract = soup.i.extract()
# decompose() 方法将当前节点移除文档树并完全销毁
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_decompose = soup.a
i_decompose = soup.i.decompose()
# 输出
print a_clear         # <a href="http://example.com/">I linked to <i></i></a>
print i_clear         # None
print a_extract       # <a href="http://example.com/">I linked to </a>
print i_extract       # <i>example.com</i>
print a_decompose     # <a href="http://example.com/">I linked to </a>
print i_decompose     # None
