# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from os import popen, getcwd, remove, system
from os.path import join
from time import strftime, localtime
from datetime import date, timedelta

reload(sys)
sys.setdefaultencoding('utf-8')

remove_list = []
result = popen('ls --full-time | grep mysql-bin').readlines()

for _ in result:
    _ = _.split()    # 把当前变量变成数组
    """['-rw-rw----', '1', 'my3306', 'mysql', '1073883249', '2018-08-22', '12:10:38.842014994', '+0800', 'mysql-bin.000600']"""
    if 'mysql-bin.index' not in _:
        remove_list.append(join(getcwd(), _[-1]))    # 把当前的名字存入到新数组

if len(remove_list) > 3:    # 如果binlog大于3个,需要处理
    for _ in remove_list[:-3]:    # 永远保留最后3个
        remove(_)
