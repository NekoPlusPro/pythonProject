# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

fi = open("score.csv","r",encoding="GBK")
fo = open("avg-score.txt","w")
t=fi.readlines()
ls = []
for i in t:
    i=i.replace('\n','')
    ls.append(i.split(','))
del ls[0]
for line in ls:
    fo.write(line[0]+':'+'{:.2f}'.format((eval(line[1])+eval(line[2])+eval(line[3]))/3.0)+'\n')
fi.close()
fo.close()
    

    
