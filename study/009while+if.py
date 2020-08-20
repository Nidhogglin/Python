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

int_month = int(input("请输入生日月："))
int_day = int(input("请输入生日日："))
print("%d月%d日" % (int_month, int_day))

n = 0
while zodiac_days[n] < (int_month, int_day):
    if (int_month, int_day) > (12, 22):
        break
    n += 1
print(zodiac_name[n])