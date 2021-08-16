fo = open('PY202.txt', 'w')
names = input('请输入各个同学职业名称，职业名称之间用空格间隔（按<Enter>键结束输入）：')
names = names.split(' ')
d = {}
for i in names:
    d[i] = d.get(i, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)
for k in ls:
    fo.write('{}:{}\n'.format(k[0],k[1]))
fo.close()
