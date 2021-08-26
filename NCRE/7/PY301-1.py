# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

fo = open("PY301-1.txt", "w")


class Horse():
    def __init__(self, category, gender, age):
        self.category = category
        self.gender = gender
        self.age = age

    def get_descriptive(self):
        self.info = "一匹" + self.age + "岁的" + self.category + self.gender + "马"
        return self.info
    def write_speed(self, new_speed):
        self.speed=new_speed
        addr = "在草原上奔跑的速度为"
        fo.write(self.get_descriptive() + "，" + addr + str(self.speed) + "km/h。")


a=Horse('阿拉伯','公','12')

a.write_speed('50')
fo.close()
