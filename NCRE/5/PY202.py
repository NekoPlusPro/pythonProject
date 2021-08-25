# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

fo = open("PY202.txt","w")
def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
ls = [51,33,54,56,67,88,431,111,141,72,45,2,78,13,15,5,69]
lis = []
for i in ls:
    if prime(i) == False:
        lis.append(i)
fo.write(">>>{}，列表长度为{}".format(lis,len(lis)))
fo.close()
