txt=input("请输入类型序列：")
fo=open("PY202.txt", "w")
li=txt.split(" ")
d={}
for i in li:
    d[i]=d.get(i,0)+1
    '''if d.get(i,0)!=0:
        d[i]+=1
    else:
        d[i]=1'''
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for k in ls:
    fo.write("{}:{}\n".format(k[0],k[1]))
fo.close()



