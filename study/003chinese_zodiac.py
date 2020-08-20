chinese_zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

print(chinese_zodiac[0])
# 切片操作符：‘:’
print(chinese_zodiac[0:4])

print(chinese_zodiac[-1])

year = 2018

t = year % 12

print(t, chinese_zodiac[year % 12 - 4])

# 成员关系操作符：'in'、'not in'
print('狗' in chinese_zodiac)

print('猪' not in chinese_zodiac)

# 连接操作符：'+'
print(chinese_zodiac+'abcd')

# 重复操作符：'*'+整数
print(chinese_zodiac * 3)