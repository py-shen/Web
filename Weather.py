# -*- coding: utf8 -*-

from urllib import request
import gzip
cityname = request.quote(input('请输入要查的城市名称： ') + '市')
# print(cityname)
content = request.urlopen('http://wthrcdn.etouch.cn/weather_mini?city=%s' % cityname).read()
try:
	web = gzip.decompress(content).decode('utf8')
except:
	web = content.decode('utf8')
print(web)
result = {}





# print(type(web))
# file = open('baidu.html', 'w')
# file.write(web)
# file.close()

