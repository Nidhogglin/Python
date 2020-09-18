#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/15 16:26

from datetime import datetime, date, timedelta, tzinfo, timezone
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call:', func.__name__)
        func(*args, **kw)
        print(func.__name__, 'end\n')
    return wrapper


@log
def demo1():
    now = datetime.now()
    print(now)
    print(type(now))
    print(date.today())


# datetime转换为timestamp
@log
def dt2ts():
    dt = datetime(2020, 10, 1, 12, 20)
    print(dt)
    print(dt.timestamp())


# timestamp转换为datetime
@log
def ts2dt():
    t = 1429417200.0
    print(t)
    print(datetime.fromtimestamp(t))  # 本地时间
    print(datetime.utcfromtimestamp(t))  # UTC时间


# str转换为datetime
@log
def str2dt():
    now = datetime.now()
    today = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    print(today)


# datetime转换为str
@log
def dt2str():
    now = datetime.now()
    print(now.strftime('%a, %b %d %Y %H:%M'))

# datetime加减
@log
def datecul():
    now = datetime.now()
    print(now)
    print(now + timedelta(hours=10))
    print(now - timedelta(days=2, minutes=30))


@log
def local2utc():
    tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
    now = datetime.now()
    print(now)
    dt = now.replace(tzinfo=tz_utc_8)
    print(dt)


# 时区转换
@log
def utcchange():
    # 拿到UTC时间，并强制设置时区为UTC+0:00:
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)
    # astimezone()将转换时区为北京时间:
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_dt)
    # astimezone()将转换时区为东京时间:
    tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt)
    # astimezone()将bj_dt转换时区为东京时间:
    tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt2)

if __name__ == '__main__':
    # demo1()
    # dt2ts()
    # ts2dt()
    # str2dt()
    # dt2str()
    # datecul()
    local2utc()
    utcchange()