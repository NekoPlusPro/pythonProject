# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

fo = open("PY202.txt","w")
data = input("请输入课程名及对应的成绩：")  # 课程名 考分
di={}
sum=0
while data:
    t=data.split(' ')
    di[t[0]]=t[1]
    sum+=eval(t[1])
    data = input("请输入课程名及对应的成绩：")
li=list(di.items())
li.sort(key=lambda x:x[1],reverse=True)
fo.write("最高分课程是{} {}, 最低分课程是{} {}, 平均分是{:.2f}".format(li[0][0],li[0][1],li[-1][0],li[-1][1],sum/len(li)))
fo.close()
