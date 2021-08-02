#import jieba
ro=open("小女孩.txt")
fo=open("PY301-1.txt","w")
txt=ro.read()
#li=jieba.lcut(txt)
d={}
sieve='，。？！《》·、——=+-%@（）‘’“”：；'
for i in txt:
    if i in sieve :
        '''过滤掉标点符号'''
        continue
    else:
        d[i]=d.get(i,0)+1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
fo.write("{}:{}".format(ls[0][0],ls[0][1]))
fo.close()