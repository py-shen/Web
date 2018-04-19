# -*- coding: utf8 -*-

from urllib import request
import gzip
import json
# 使用request.quote对中文网址进行转码处理
cityname = request.quote(input('请输入要查的城市名称： ') + '市')

content = request.urlopen('http://wthrcdn.etouch.cn/weather_mini?city=%s' % cityname).read()
try:
	# 使用gzip.decompress对网页抓取的内容进行gzip解压并转码utf8
	web = gzip.decompress(content).decode('utf8')
except:
	web = content.decode('utf8')
if web == ('{"status":1002,"desc":"invilad-citykey"}'):
	print('城市名称错误！')
	quit()
else:
	info = json.loads(web)
	a = info['data']
	b = a['forecast']
	c = b[0]
	print('%s // %s // %s ~ %s' % (c['date'], c['type'], c['low'], c['high']))


