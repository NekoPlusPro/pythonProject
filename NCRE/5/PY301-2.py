fi=open("arrogant.txt",'r')
fo=open("arrogant-sort.txt",'w')
reader=fi.read().replace('\n','')
d = {}
for i in reader:
    d[i]=d.get(i,0)+1
ls =list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for j in range(10):
    fo.write("{}:{}\n".format(ls[j][0],ls[j][1]))
fo.close()
