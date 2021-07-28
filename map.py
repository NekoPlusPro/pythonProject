import csv
rname = 'data2.csv'
wname='shift.csv'

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
    return mmax

with open(rname) as r:
    with open(wname,'w',encoding='utf-8',newline='') as w:
        reader = csv.reader(r)
        writer = csv.writer(w)
        header_row = next(reader)
        print(header_row)
        for row in reader:
            if lcsubstr(row[4],row[5])>=3:
                writer.writerow(row)

