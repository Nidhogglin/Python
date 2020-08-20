# 第一题
str1 = input("请输入一个字符串：")
# print(len(str1))
if len(str1) == 10:
    print("1. 字符串“%s”长度为10" % str1)
else:
    print("1. 字符串“%s”长度不为10" % str1)

# 第二题
num = int(input("2. 请输入一个1-40的数字："))
if num > 30:
    print("31-40")
elif num > 20:
    print("21-30")
elif num > 10:
    print("11-20")
else:
    print("1-10")

# 第三题
for n in range(1, 101):
    if n % 2 == 0:
        print(n)

# 第四题
x = 1
while x <= 100:
    if x % 3 == 0:
        print(x)
    x += 1 