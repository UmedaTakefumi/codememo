#!/usr/bin/env python
# -*- coding: utf8 -*-

# 情報源:
#   http://d.hatena.ne.jp/yuheiomori0718/20120122/1327217763

from datetime import datetime, timedelta

start = datetime.strptime('201201', '%Y%m')
end = datetime.strptime('201202', '%Y%m')

print "----"
print start
print end
print "----"

#start = datetime.strptime('20140109', '%Y%m')
#end   = datetime.strptime('20160531', '%Y%m')

def daterange(start_date, end_date):
    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)

for i in daterange(start, end):
    # 処理
    print i





