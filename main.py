# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


import webbrowser as web
from urllib.parse import quote
from urllib import request
city="jiujing"
city2="jj"
com=quote("国窖庄园")
aurl="https://"+city+".anjuke.com/community/?kw="+com
burl="https://"+city+".ke.com/xiaoqu/rs"+com
lurl="https://"+city+".lianjia.com/xiaoqu/rs"+com
zurl="http://"+city+".xiaoqu.zhuge.com/v_"+com+"_/"
aurl2="https://"+city2+".anjuke.com/community/?kw="+com
burl2="https://"+city2+".ke.com/xiaoqu/rs"+com
lurl2="https://"+city2+".lianjia.com/xiaoqu/rs"+com
zurl2="http://"+city2+".xiaoqu.zhuge.com/v_"+com+"_/"
web.open(aurl)
web.open(burl)
web.open(lurl)
web.open(zurl)
web.open(aurl2)
web.open(burl2)
web.open(lurl2)
web.open(zurl2)