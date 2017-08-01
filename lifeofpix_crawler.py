import requests
from bs4 import BeautifulSoup
from threading import Thread

url = 'http://www.lifeofpix.com'

def down_pic(link):
	print('downing:' + link)
	pic = requests.get(link)
	filename = link.split('/')[-1]
	with open('pics/' + filename, 'wb') as f:
		f.write(pic.content)

for i in range(2):
	User_Agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
	header = {'User_Agent': User_Agent}
	req = requests.get(url, headers=header)
	html = req.text
	soup = BeautifulSoup(html, 'lxml')
	soup_pic = soup.find_all('div', class_='node large')

	for link  in soup_pic:
		link = link.img['src']
		t = Thread(target=down_pic, args=(link,))
		t.start()

	current_page = soup.find_all('div', class_="current")
	current_page = current_page[0].text
	next_page = int(current_page) + 1
	url = 'http://www.lifeofpix.com/page/%d' % next_page


