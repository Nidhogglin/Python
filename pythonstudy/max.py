#  找出数组中相邻两个数之和最大的一组

def fmax(a):
    max = a[0] + a[1]
    index = 0
    for i in range(1, len(a) - 1):
        if (a[i] + a[i+1]) > max:
            max = a[i] + a[i+1]
            index = i
    return index


a = [-1, 2, -1, 3, -1, 4, -5, 1, 6, -3]
index = fmax(a)
print("相加最大值的组合下标为：%d，%d，最大值为%d" % (index, index+1, (a[index]+a[index+1])))