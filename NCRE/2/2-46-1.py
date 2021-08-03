ro=open('PY301-vacations.csv')
reader=ro.readlines()
reader.pop(0)
ls = []
for i in reader:
    ls.append(i.split(","))
a=input("请输入节假日名称（例如，春节）：")
for j in ls:
    if a==j[1]:
        print("{}的假期位于{}-{}之间".format(j[1],j[2],j[3].replace("\n","")))#换行符别忘记去掉！！！！！
