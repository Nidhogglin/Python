zodiac_name = (
    u'摩羯座',
    u'水瓶座',
    u'双鱼座',
    u'白羊座',
    u'金牛座',
    u'双子座',
    u'巨蟹座',
    u'狮子座',
    u'处女座',
    u'天秤座',
    u'天蝎座',
    u'射手座',
)
zodiac_days = (
    (1, 20),
    (2, 19),
    (3, 21),
    (4, 20),
    (5, 21),
    (6, 22),
    (7, 23),
    (8, 23),
    (9, 23),
    (10, 24),
    (11, 23),
    (12, 22),
)

# 指定日期
(month, day) = (12, 23)
# 过滤出在指定日期前的元素
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# 求出在指定日期前的元素个数
zodiac_len = len(list(zodiac_day))
# 指定日期前的元素个数除以12取余，结果即为星座下标
print(zodiac_name[zodiac_len % 12])