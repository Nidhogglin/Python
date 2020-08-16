chinese_zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

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
# 创建字典并遍历字典,用来记录对应生肖的数量
cz_num = {}  # 声明字典
for i in chinese_zodiac:
    cz_num[i] = 0  # 往字典里添加键值对 eg：'鼠': 0
print(cz_num)
# 创建字典并遍历字典,用来记录对应星座的数量
z_num = {}
for i in zodiac_name:
    z_num[i] = 0 
print(z_num)

# 用无限循环输入生日年月日并记录对应生肖星座数量
while True:
    # 输入
    print("年份输入为-1表示结束")
    year = int(input("请输入出生年份："))
    if year == -1:
        break
    month = int(input("请输入出生月份："))
    day = int(input("请输入出生日期："))

    # 记录对应生肖数量
    cz_num[chinese_zodiac[year % 12 - 4]] += 1

    # 记录对应星座数量
    n = 0
    while zodiac_days[n] < (month, day):
        if (month, day) > (12, 22):
            break
        n += 1
    z_num[zodiac_name[n]] += 1

# 遍历生肖和星座数量
for each_key in cz_num.keys():  # 暂时还不明白+.keys()和不加的区别
    print("生肖为%s的有%d人" % (each_key, cz_num[each_key]))

for each_key in z_num:
    print("星座为%s的有%d人" % (each_key, z_num[each_key]))
