# 列表推导式
# 输出1-10之间奇数的平方

# 普通方式
alist = []
for i in range(1, 11):
    if(i % 2 == 1):
        alist.append(i * i)
print(alist)

# 推导式
blist = [i * i for i in range(1, 11) if(i % 2) == 1]
print(blist)

# 字典推导式
sex = ('男', '女', '保密')

# 普通方式
s_num1 = {}
for i in sex:
    s_num1[i] = 0
print(s_num1)

# 推导式
s_num2 = {i: 0 for i in sex}
print(s_num2)