chinese_zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
# 遍历序列（字符串、列表、元组）
for x in chinese_zodiac:
    print(x)
# 遍历数字[1, 13)
for i in range(1, 13):
    print(i)
# 变量替换
for year in range(2012, 2021):
    print("%d年出生的人属%s" % (year, chinese_zodiac[year % 12 - 4]))