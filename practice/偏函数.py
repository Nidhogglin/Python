
import functools

# base参数的值表示需要转换的值的进制，转换目标为10进制
print(int('12345', base=8))
print(int('12345', 16))
print('%x' % 74565)

# 偏函数，可以把函数的某些参数固定住
int2 = functools.partial(int, base=2)
print(int2('10101'))

# 当传入参数为函数和值时，值会作为传入函数的参数
max2 = functools.partial(max, 10)
print(max2(2, 5, 7))  # 结果为10
