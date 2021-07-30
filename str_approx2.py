import csv
import re
#文件名称
rname_1 = '上海市.csv'
rname_2 = 'unmatch.csv'
wname='match.csv'
sieve=["上海市",	'黄浦区','徐汇区','长宁区','静安区','普陀区','虹口区','杨浦区','闵行区','宝山区','嘉定区','浦东新区','金山区','松江区','青浦区','奉贤区','崇明区',]
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
    return mmax
def regu(t):
    a=t
    for i in sieve:
        a = re.sub(i, "", a)
    return a
def lcseque(s1, s2):
     # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果
    m = [ [ 0 for x in range(len(s2)+1) ] for y in range(len(s1)+1) ]
    # d用来记录转移方向
    d = [ [ None for x in range(len(s2)+1) ] for y in range(len(s1)+1) ]

    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:            #字符匹配成功，则该位置的值为左上方的值加1
                m[p1+1][p2+1] = m[p1][p2]+1
                d[p1+1][p2+1] = 'ok'
            elif m[p1+1][p2] > m[p1][p2+1]:  #左值大于上值，则该位置的值为左值，并标记回溯时的方向
                m[p1+1][p2+1] = m[p1+1][p2]
                d[p1+1][p2+1] = 'left'
            else:                           #上值大于左值，则该位置的值为上值，并标记方向up
                m[p1+1][p2+1] = m[p1][p2+1]
                d[p1+1][p2+1] = 'up'
    (p1, p2) = (len(s1), len(s2))
    s = []
    while m[p1][p2]:    #不为None时
        c = d[p1][p2]
        if c == 'ok':   #匹配成功，插入该字符，并向左上角找下一个
            s.append(s1[p1-1])
            p1-=1
            p2-=1
        if c =='left':  #根据标记，向左找下一个
            p2 -= 1
        if c == 'up':   #根据标记，向上找下一个
            p1 -= 1
    s.reverse()
    return ''.join(s)

#读写器
with open(rname_1) as s:
    with open(rname_2) as u:
      with open(wname, 'w', encoding='utf-8', newline='') as w:
        readers = csv.reader(s)
        readeru = csv.reader(u)
        writer = csv.writer(w)
        next(readers)
        next(readeru)
        header_row=["uname","sname","id","appr"]
        writer.writerow(header_row)
        dic={}
        lis=[]
        for srow in readers:
            dic[srow[0]]=regu(srow[1])
        for urow in readeru:
            lis.append(urow[0])
        for i in lis:
            wrow = [i,"null","null",-1]
            i = regu(i)
            for key,value in dic.items():
                a=lcsubstr(i,value)
                if a>wrow[3] :
                    wrow[1],wrow[2],wrow[3] = value,key,a
            writer.writerow(wrow)
