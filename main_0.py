# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
a=eval(input())
b=eval(input())
if b>a:
    c=b
    b=a
    a=c
def fun(n):
    x=pow(n,4)-33*pow(n,3)+217*pow(n,2)+825*n-6050
    return x
def bis(left,right):
    while right-left>0.00001:
        mid=(left+right)/2.0
        if fun(left)==0:
            return left
        elif fun(right)==0:
            return right
        elif fun(left)*fun(mid)<0:
            right=mid
        else:
            left=mid
    return left

print("%.2f"%bis(b,a))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
