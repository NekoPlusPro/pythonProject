# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

def judge_year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return str(year)+'是闰年'
    else:
        return str(year)+'不是闰年'
year = eval(input("请输入年份："))
print(judge_year(year))

