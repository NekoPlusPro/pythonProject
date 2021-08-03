n = eval(input('请输入数量：'))
price = 150
if n == 1:
    cost = n * price
elif n == 2 or n == 3:
    cost = int(n * price * 0.9)
elif 4 <= n <= 9:
    cost =  int(n * price * 0.8)
else:
    cost = int(n*price*0.7)
print('总额为：', cost)
