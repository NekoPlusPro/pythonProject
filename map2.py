import csv
import re
rname = '220102.csv'
wname='result.csv'

def lcsubstr(s1, s2):
    m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]
    mmax=0
    p=0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                m[i+1][j+1]=m[i][j]+1
                if m[i+1][j+1]>mmax:
                    mmax=m[i+1][j+1]
                    p=i+1
    return s1[p-mmax:p],mmax

with open(rname) as r:
    with open(wname,'w',encoding='utf-8',newline='') as w:
        reader = csv.reader(r)
        writer = csv.writer(w)
        header_row = next(reader)
        header_row.extend(["re_res_name","threshold","appr","subname"])
        writer.writerow(header_row)
        print(header_row)
        for row in reader:
            row.append(re.sub("\\(.*?\\)","",row[5]))
            row.append(3 if len(row[8])>4 else 2)
            t=lcsubstr(row[4],row[8])
            row.append(t[1])
            row.append(row[4].replace(t[0],""))
            writer.writerow(row)


