import csv
import re

rname = '220102.csv'
wname = 'result3.csv'
sieve = ["山庄", "庄园", "学院", "小区",
         "家园", "花园", "国际", "别墅",
         "中心", "广场", "公馆", "公园",
         "大厦", "小镇", "公寓", "社区", "嘉园"]


def lcsubstr(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    mmax = 0
    p = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - mmax:p], mmax


def regu(t):
    a = re.sub("\\(.*?\\)", "", t)
    a = re.sub("[·.|-]","",a)
    for i in sieve:
        a = re.sub(i, "", a)
    return a


def uncn(f):
    pat = re.compile(r'[\u4e00-\u9fa5]')
    b = re.sub("[·.|-]"," ",f)
    return '|'.join(re.sub(pat, " ", b).split())


with open(rname) as r:
    with open(wname, 'w', encoding='utf-8', newline='') as w:
        reader = csv.reader(r)
        writer = csv.writer(w)
        header_row = next(reader)
        header_row.extend(["re_res_name",'re_len', "appr", "subname"])
        writer.writerow(header_row)
        print(header_row)
        for row in reader:
            t=regu(row[5])
            row.append(t)
            row.append(len(t))
            row.append(lcsubstr(re.sub("[·.|-]","",row[4]), row[8])[1])
            row.append(uncn(row[4]))
            writer.writerow(row)
