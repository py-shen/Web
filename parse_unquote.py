import urllib.parse


def quote(x):
	return urllib.parse.quote(x)


# print(urllib.parse.unquote("http://wthrcdn.etouch.cn/weather_mini?city=%E4%B8%8A%E6%B5%B7%E5%B8%82"))
# print('http://wthrcdn.etouch.cn/weather_mini?city='+ urllib.parse.quote("上海市"))