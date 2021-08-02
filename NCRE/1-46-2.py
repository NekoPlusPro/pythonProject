#import jieba
ro=open("小女孩.txt")
fo=open("PY301-2.txt","w")
txt=ro.read()
#li=jieba.lcut(txt)
d={}
#sieve='，。？！《》·、——=+-%@（）‘’“”：；'
for i in txt:
    if i == "\n" :
        '''过滤掉换行符'''
        continue
    else:
        d[i]=d.get(i,0)+1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    fo.write("{}".format(ls[i][0]))
fo.close()