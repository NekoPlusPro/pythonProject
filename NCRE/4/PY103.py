# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

n = eval(input("请输入一个数字:"))
print("{:+^11}".format(chr(n-1)+chr(n)+chr(n+1)))