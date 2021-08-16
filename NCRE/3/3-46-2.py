import  re
fi = open("论语-原文.txt",'r')
fo = open("论语-提纯原文.txt",'w')
reader=fi.readlines()
for line in reader:
    fo.write(re.sub('\([0-9]\)','',line))

