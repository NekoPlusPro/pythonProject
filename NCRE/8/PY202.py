# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

import math
try:
    a = eval(input('请输入底数：'))
    b = eval(input('请输入真数：'))
    c = math.log(b,a)
except ValueError:
    print('底数和真数必须大于0')
except ZeroDivisionError:
    print('底数不能为1')
except NameError:
    print('输入必须为实数')
else:
    print(c)
