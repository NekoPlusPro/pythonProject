# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

intxt = input("请输入明文：")
for i in intxt:
    if 'a' <= i <= 'z':
        print(chr(97 + (ord(i) - 97 + 3) % 26),end='')
    elif 'A' <= i <= 'Z':
        print(chr(65 + (ord(i) - 65 + 3) % 26),end='')
    else:
        print(i,end='')