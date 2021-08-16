fi=open('sensor.txt','r')
fo=open('earpa001.txt','w')
reader=fi.readlines()
for line in reader:
    t=line.split(',')
    if ' earpa001' in t[1]:
        fo.write('{},{},{},{}'.format(t[0],t[1],t[2],t[3]))
fo.close()#文件写一定要及时关闭！！！！！！不然写不进去


