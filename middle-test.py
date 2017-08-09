#读取 report.txt文件中的成绩
with open('report.txt', 'r', encoding='utf-8') as f:
	lines = f.readlines()

#统计每名学生总成绩、计算平均并从高到低重新排名
results = []
for line in lines:
	data = line.split()
	sum = 0
	for i in data[1:]:
		sum += int(i)
	data.append(sum)
	every_avg = round(sum / 9.0, 2)
	data.append(every_avg)
	results.append(data)
results.sort(key=lambda x: x[-1], reverse=True)

#汇总每一科目的平均分和总平均分
avg = []
for i in range(1,12):
	spl_sum = 0
	for j in results:
		spl_sum += float(j[i])
		spl_avg = round(spl_sum/len(results), 2)
	avg.append(spl_avg)
avg.insert(0,'平均')
results.insert(0,avg)

#替换60分以下的成绩为“不及格”
for i in results:
	for j in i[1:10]:
		if float(j) < 60:
			i[i.index(j)] = '不及格'

#添加名次
rank = 0
for i in results:
	i.insert(0,rank)
	rank += 1
title = ['名次','姓名','语文', '数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
results.insert(0, title)

#另存为一个新文件
with open('new_report.txt', 'w', encoding='utf-8') as f:
	for line in results:
		for index in range(len(line)):
			line[index] = str(line[index])
		text = '  '.join(line) + '\n'
		f.writelines(text)
