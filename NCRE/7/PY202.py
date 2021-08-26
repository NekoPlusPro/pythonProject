# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

lower = int(input('输入区间最小值：'))
upper = int(input('输入区间最大值：'))
def pri(a):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
for num in range(lower+1,upper):
    if pri(num) is True:
        print(num,end=' ')
