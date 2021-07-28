import csv
from xpinyin import Pinyin
import webbrowser as web
from urllib.parse import quote

fname = 'dp.csv'
with open(fname) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    names, citys = [], []
    for row in reader:
        names.append(row[0])
        citys.append(row[4].replace("市", ""))
p = Pinyin()
for n in range(0, 50):
    city = p.get_pinyin(citys[n], '')
    city2 = p.get_initials(citys[n], '').lower()
    com = quote(names[n])
    # jurl="http://"+ city +".jiwu.com/esf/list-key"+com+".html"
    # jurl2="http://"+ city2 +".jiwu.com/esf/list-key"+com+".html"
    # zfurl="https://www.creprice.cn/ha/search.html?key="+com
    # furl="https://fangjia.fang.com/pghouse-c0"+city+"/h315-s11-kw"+com+"/"
    # furl2="https://fangjia.fang.com/pghouse-c0"+city2+"/h315-s11-kw"+com+"/"
    # furl ="https://"+ city+ ".esf.fang.com/housing/__0_0_0_0_1_0_0_0/"+com
    # furl2 = "https://" + city2 + ".esf.fang.com/housing/__0_0_0_0_1_0_0_0/" + com
    # aurl = "https://" + city + ".anjuke.com/community/?kw=" + com
    # aurl2 = "https://" + city2 + ".anjuke.com/community/?kw=" + com
    surl = "https://" + city + ".focus.cn/loupan/?q=" + com
    surl2 = "https://" + city2 + ".focus.cn/loupan/?q=" + com
    web.open(surl)
    web.open(surl2)
    # web.open(zfurl)
    # w=input(citys[n]+" "+names[n])
