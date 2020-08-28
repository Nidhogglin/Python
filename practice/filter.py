# filter函数

def is_odd(n):
    return n % 2 == 1


a = filter(is_odd, [1, 2, 3, 4, 5, 6])
print(a)
print(list(a))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', 'B', 'C', None, ' '])))


b = '111'
print(b.strip())


def jishu():
    n = 1
    while True:
        n += 2
        yield n


for i in jishu():
    print(i)
    if i > 10:
        break


def List(n):
    return lambda x: x % n > 0


def result():
    n = 2
    it = jishu()
    while True:
        yield n
        n = next(it)
        it = filter(List(n), it)


def is_palindrome(n):
    s =str(n)
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return 0
    return 1


if __name__ == '__main__':
    for i in result():
        if i >100:
            break
        print(i)

    print(list(filter(is_palindrome, range(1,200))))
