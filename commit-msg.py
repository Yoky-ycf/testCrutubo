#!/usr/bin/env python
# -*- coding: utf-8
import sys, os, re
from subprocess import check_output


reload(sys)
sys.setdefaultencoding('gbk')

# 收集参数，第一个参数是commit的信息的文件
commit_msg_filepath = 'sys.argv[1]'
# 读取文件
file = open('D:/data/test.txt','a+')
logo = 'change'
for ff in file:
      if(ff.startswith('OA-136')):
            print('通过')
            logo = 'for_change'
            sys.exit(0)

if(logo.startswith("change")):
    print "commit-msg: ERROR! The commit message must start with AO"
    print '不通过反反复复'
    sys.exit(1)
