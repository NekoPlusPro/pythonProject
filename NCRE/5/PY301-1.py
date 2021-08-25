fi=open("arrogant.txt",'r')
fo=open("PY301-1.txt",'w')
reader=fi.read().replace('\n','')
d = {}
for i in reader:
    d[i]=d.get(i,0)+1
ls =list(d.items())
for j in ls:
    fo.write("{}:{}\n".format(j[0],j[1]))
fo.close()
