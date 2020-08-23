#  求数组中连续多个元素求和最大的组合

def MaxSubArray1(a):
    max = 0
    for i in range(1, len(a)+1):  # 连续求和的元素个数
        for j in range(0, len(a)-i+1):  # 元素求和开始的下标
            sum = 0  # sum存储每次元素相加的和，循环开始时重置为零
            for k in range(j, j+i):  # 元素求和开始的下标和求和求和元素个数
                sum += a[k]  # 连续多和元素求和
            if sum > max:  # 判断当次元素的和是否大于预设的最大值
                max = sum  
                index = [j, j+i-1]  # 用列表存储最大和的组合的初始下标和最后下标
    return index, max  # 返回元素组合和最大值


def MaxSubArray2(a):
    s = 0
    m = 0
    for i in range(len(a)):
        s = a[i]
        m = max(s, m)
        for j in range(i+1, len(a)):
            s += a[j]
            m = max(s, m)
    return m


def MaxSubArray3(a):
    max_cru = -float('inf')
    max_pre = -float('inf')
    for i in a:
        max_cru = max(max_cru + i, i)
        max_pre = max(max_cru, max_pre)
    return max_pre, max_cru


def MaxSubArray4(a):
    for i in range(1, len(a)):
        a[i] += max(a[i-1], 0)
    return a[-1]


def main():
    a = [1, -3, 4, -2, 5, -7, 6, -1]

    print(MaxSubArray2(a))
    print(MaxSubArray3(a))
    print(MaxSubArray4(a))


    index, max = MaxSubArray1(a)
    print("和为最大值的组合下标为：%d至%d，最大值为：%d" % (index[0], index[1], max))


if __name__ == '__main__':
    main()
