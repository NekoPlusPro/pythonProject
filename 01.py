list =[]
for i in range(10):
    list.append(eval(input()))
for j in range(10):
    for k in range(j):
        if list[j]<=list[k]:
            a=list[j]
            list[j]=list[k]
            list[k]=a
for l in list:
    print(l)
