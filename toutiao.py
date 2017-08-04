import requests, csv

url_1 = 'http://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time='
headers = {
'Cookie':'UM_distinctid=15da2459d0a12c-0604010def216b-5c153f17-e1000-15da2459d0b49a; uuid="w:d446ba6feeb947d2ad76590b43fa670a"; _ga=GA1.2.1491577557.1501666109; csrftoken=984ff04bc688740dd05e7ac273f352aa; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=pdd8nr3eu1501815992992; CNZZDATA1259612802=260495980-151661052-https%253A%252F%252Fwww.baidu.com%252F%7C1501812252; tt_webid=6449606271682332173',
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
}

max_behot_time = '0'
info = []
def get_info(url):
	global  max_behot_time, info
	req = requests.get(url, headers=headers)
	content = req.json()
	next_page = content['next']
	max_behot_time = next_page['max_behot_time']
	print(max_behot_time)
	for item in content['data']:
		lst = []
		try:
			lst.append(item['title'])
			lst.append(item['abstract'])
			lst.append(item['comments_count'])
			info.append(lst)
		except Exception as e:
			print(e)
			continue
	return max_behot_time
for i in range(5):
	url = url_1 + str(max_behot_time)
	max_behot_time = get_info(url)

with open('toutiao.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['标题', '概述', '评论数'])
    for data in info:
        writer.writerow(data)