s = eval(input("请输入一个数字："))
ls = [0]
for i in range(65,91):
    ls.append(chr(i))
print("输出大写字母：{}".format(ls[s]))
