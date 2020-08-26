# sequence = [1, 1]
#
# n = int(input("请输入要查看值的项数："))
#
# for i in range(2, n):
#     sequence.append((sequence[i-1] + sequence[i-2]))
#
# print(sequence[n-1])


# x = 1
# y = 1
# for i in range(2, n + 1):
#     z = y + x
#     x = y
#     y = z
#
# print(z)


# def fn(n):
#     if n < 2:
#         return 1
#     return fn(n-1) + fn(n-2)

def fib(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a+b

    return a

# nstr = iter("12345")
#
# for i in range(5):
#     print(next(nstr))



if __name__ == '__main__':

    n = int(input("请输入要查看值的项数："))
    print(fib(n))

