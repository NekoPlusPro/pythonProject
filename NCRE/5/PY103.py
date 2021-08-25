import jieba
s = input("请输入一个中文字符串，包含标点符号：")
m =jieba.lcut(s)
print("中文词语数：{}".format(len(m)))
