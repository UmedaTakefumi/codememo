#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

args = sys.argv

pp.pprint(args)

print("---------------------------")

num=0

for value in args:
  print("第{}引数: {} ".format(num,value))
  num+=1
"""
##; 情報源

* http://www.python-izm.com/contents/basis/command_line_arguments.shtml
"""
