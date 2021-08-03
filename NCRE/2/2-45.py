fo = open("PY202.txt", 'w')
data = input("请输入一组人员的姓名、性别、年龄：")
num = 0
age = 0
female = 0
while data:
    data = data.split(" ")
    num += 1
    age += int(data[2])
    female += 1 if data[1] == "女" else 0
    data = input("请输入一组人员的姓名、性别、年龄：")
ave = age / num
fo.write("平均年龄是{:.1f} 女性人数是{}".format(ave, female))
fo.close()
