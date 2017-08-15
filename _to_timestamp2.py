# -*- coding: utf-8 -*-
__author__ = 'Edward'
import re
from datetime import datetime,timezone,timedelta
def to_timestamp(dt_str,tz_str):
    cday=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    n=int(re.split('[C\:]',tz_str)[1])
    #n=int(re.match(r'UTC([+-]\d+)\:(\d+)',tz_str).group(1))
    return cday.replace(tzinfo=timezone(timedelta(hours=n))).timestamp()
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
