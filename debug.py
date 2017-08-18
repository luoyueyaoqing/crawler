import urllib.request
import requests

url1 = 'http://m.weather.com.cn/data3/city.xml'
#req = urllib.request.urlopen(url1)
req = requests.get(url1)
data = req.content
#print('data:', type(data), repr(data))
content1 = data.decode('utf8')
#print('content1:', content1)
provinces = content1.split(',')
#print(provinces)
result = 'city = {\n'
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces[1:]:
#	print('p:', repr(p))
	p_code = p.split('|')[0]
#	print('p_code:',type(p_code), repr(p_code))
	url2 = url % p_code
#	print('url2:', url2)
	r = urllib.request.urlopen(url2)
	d = r.read()
	content2 = d.decode('utf8')
#	print('content2:',content2)
	cities = content2.split('|')
#	print('cities:', cities)
	for c in cities:
#		print('c:', repr(c))
		c_code = c.split('|')
#		print('c_code:', c_code)
		url3 = url % c_code[0]
#		print('url3:', url3)
		try:
			content3 = urllib.request.urlopen(url3).read().decode('utf8')
	#		print('content3;', content3)
			districts = content3.split(',')
	#		print('districts:', districts)
		except:
			continue
		for d in districts:
#			print('d:', repr(d))
			d_pair = d.split('|')
#			print('d_pair:', repr(d_pair))
			d_code = d_pair[0]
#			print('d_code:', d_code)
			name = d_pair[1]
#			print(name)
			url4 = url % d_code
			content4 = urllib.request.urlopen(url4).read().decode('utf8')
#			print('content4:', content4)
			code = content4.split('|')[1]
			line = "    '%s': '%s',\n" % (name, code)
			result += line
			print(name + ':' + code)
result += '}'
f = open('city.py', 'w')
f.write(result)
f.close()