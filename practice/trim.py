# 去除字符串前面和后面空格

def trim(s):
    i, j = 0, -1
    if s == '':
        return s

    while i < len(s) and s[i] == ' ':
        i += 1

    while -j < len(s) and s[j] == ' ':
        j -= 1

    if j == -1:
        j = len(s)
    if i == len(s):
        s = ''
    else:
        s = s[i:j+1]

    return s


if __name__ == '__main__':
    print(trim('sssd'))
