import requests
from lxml import etree

url = "https://www.qiushibaike.com/"
data_all = ''

for i in range(3):
	req = requests.get(url)
	html = req.text
	tree = etree.HTML(html)
	result = tree.xpath('//div[contains(@class, "article block untagged mb15")]')
	for div in result:
		author = div.xpath('.//h2/text()')
		data_all += (author[0] + ' \n')
		if (author[0] == u'匿名用户'):
			pass
		else:
			age = div.xpath('.//div[@class="articleGender manIcon"]/text()|.//div[@class="articleGender womenIcon"]/text()')[0]
			data_all += ('年龄:' + age[0] + ' ')
			gender = div.xpath('.//div')[0].attrib['class']
			if (gender == 'articleGender womenIcon'):
				data_all += u'女'
			else:
				data_all += u'男'
		content = div.xpath('.//div[@class="content"]/span/text()')
		for p in content:
			data_all += p
			data_all += '\n'
		stats_vote = div.xpath('.//span[@class="stats-vote"]/i/text()')
		data_all += ('点赞数:' + stats_vote[0] + ' ')
		stats_comments = div.xpath('.//span[@class ="stats-comments"]/a/i/text()')
		data_all += ('评论数:' + stats_comments[0] + '\n')
		data_all += ('=========================' + '\n')

	current_page = tree.xpath('//li/span[@class="current"]/text()')
	next_page = int(current_page[0]) + 1
	url = "https://www.qiushibaike.com/8hr/page/%d/" % next_page

with open('qiushi_joke.txt', 'w', encoding='utf-8') as f:
	f.write(data_all)