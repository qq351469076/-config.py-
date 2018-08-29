# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from os import popen, getcwd, remove
from os.path import join
from time import strftime, localtime
from datetime import date, timedelta

reload(sys)
sys.setdefaultencoding('utf-8')


remove_list = []
date = str(date.today() - timedelta(days=3))
result = popen('ls --full-time | grep mysql-bin').readlines()
for _ in result:
    if 'mysql-bin.index' not in _:
        # ['-rw-rw----', '1', 'my3306', 'mysql', '1073883249', '2018-08-22', '12:10:38.842014994', '+0800', 'mysql-bin.000600']
        if _.split()[5] < date:
	    remove_list.append(join(getcwd(), _.split()[-1]))
if remove_list:
    print remove_list
    for temp in remove_list:
		remove(temp)
