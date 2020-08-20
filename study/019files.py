# 文件的输入和输出
# 文件输入
file1 = open('name.txt', 'w')  # 'w'：允许写入，会覆盖原内容
file1.write('1 刘备\n')  # 写入操作
file1.close()  # 关闭，同时保存，打开后必须关闭

# 在文件中增加输入
file2 = open('name.txt', 'a')  # a：在原内容后增加内容
file2.write('2 关羽\n3 张飞\n')
file2.close()

# 文件输出
file3 = open('name.txt', 'r')  # 写'r'或者不写：只读
print(file3.read())
file3.close()

# 读取其中一行
file4 = open('name.txt')
print(file4.readline(3)) # 括号里的参数代表字符数，不加参数读取第一行全部内容
file4.close()

# 逐行读取
file5 = open('name.txt')
for line in file5.readlines():
    print(line)
    # print('=====')
file5.close()

# 文件指针：文件操作位置指示器
file6 = open('name.txt')
print('当前指针位置：%s' % file6.tell())
print('读取的内容：%s' % file6.read(3)) # 读取3个字符，“刘”占了2个字节
print('当前指针位置：%s' % file6.tell())  # “刘”占了2个字节，所以指针在4

file6.seek(1)  # 一个参数，表示跳转到该下标
print('当前指针位置：%s' % file6.tell())
print('读取的内容：%s' % file6.read(3))

file6.seek(5,0)  # 两个参数，左边的代表移动位数，右边的代表开始位置：0代表从开头，1代表从当前位置，2代表从末尾
print('当前指针位置：%s' % file6.tell())