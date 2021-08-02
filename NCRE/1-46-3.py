ro=open("小女孩.txt")
fo=open("小女孩——频次排序.txt","w")
txt=ro.read()
d={}
for i in txt:
    d[i]=d.get(i,0)+1
del d['\n']
del d[' ']
#使用删除方法直接排除
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in ls[:-1]:
    fo.write(i[0]+':'+str(i[1])+',')
    #排除最后一行，最后一行后没有逗号
fo.write(ls[-1][0]+':'+str(ls[-1][1]))
fo.close()