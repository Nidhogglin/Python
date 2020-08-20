# 读取文件内容并进行操作

def file_read():
    file_1 = open('log.txt')
    sum = 0
    for line in file_1.readlines():
        a = line.split(' ')
        sum += (int(a[5])+int(a[7]))
    return sum


print(file_read())