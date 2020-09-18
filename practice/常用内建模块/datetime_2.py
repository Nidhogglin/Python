#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/18 10:51

from datetime import datetime, timezone, timedelta
import re


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz = re.match(r'^(UTC)([\-]\d{1,2}|[\+]\d{1,2})', tz_str)
    dt_bj = dt + timedelta(hours=8-int(tz.group(2)))
    tz_utc_8 = timezone(timedelta(hours=8))
    dt_bj = dt_bj.replace(tzinfo=tz_utc_8)
    ts = dt_bj.timestamp()
    print(dt, tz, ts)


def to_timestamp2(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz = re.match(r'^(UTC)([\-]\d{1,2}|[\+]\d{1,2})', tz_str)
    tz_utc_n = timezone(timedelta(hours=int(tz.group(2))))
    print(tz_utc_n)
    dt = dt.replace(tzinfo=tz_utc_n)
    print(dt)
    print(dt.timestamp())
    dt_bj = dt.astimezone(timezone(timedelta(hours=8)))
    print(dt_bj)
    print(dt_bj.timestamp())


if __name__ == '__main__':
    # to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    to_timestamp2('2015-5-31 15:10:30', 'UTC-10:00')