# 汉诺塔移动方式

def hanoi(n, a='A', b='B', c='C'):
    global count
    if n == 1:
        print(a, '-->', c)
        count += 1
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)


if __name__ == '__main__':
    count = 0
    hanoi(3)
    print("步数:", count)