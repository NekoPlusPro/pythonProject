
fi = open("论语.txt",'r',encoding='GBK')
fo = open("论语-原文.txt",'w')
reader=fi.readlines()
for i in range(len(reader)) :
    if reader[i]=='\n':
        continue
    elif '原文' in reader[i]:
        fo.write(reader[i+2].lstrip())
