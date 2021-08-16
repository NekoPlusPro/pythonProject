fi=open('earpa001.txt','r')
fo=open('earpa001_count.txt','w')
d = {}
reader=fi.readlines()
for line in reader:
  line=line.split(',')
  d[(line[2],line[3])]=d.get((line[2],line[3]),0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True) # 该语句用于排序
for i in ls:
  fo.write('{}-{},{}\n'.format(i[0][0],i[0][1].replace('\n',''),i[1]))
fo.close()