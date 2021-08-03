ro = open('PY301-vacations.csv')
reader = ro.readlines()
reader.pop(0)
ls = []
for i in reader:
    t = i.split(",")
    t[3] = t[3].replace("\n", '')
    ls.append(t)
while True:
    a = input("请输入节假日序号：")
    b = a.split(' ')
    for i in b:
        flag=False
        for j in ls:
            if i == j[0]:
                s = ' '.join(j[2]).split(' ')
                e = ' '.join(j[3]).split(' ')
                print("{}({})的假期是{}月{}日至{}月{}日之间".format(j[1],j[0],s[0]+s[1],s[2]+s[3],e[0]+e[1],e[2]+e[3]))
                flag=True
        if flag == False:
            print("输入节假日编号有误！")