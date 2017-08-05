import pymongo
import requests

# 所有 API 接口示例页面
# srs = 'http://moonlib.com/606.html'

client = pymongo.MongoClient()
db = client.wangyi
db_playlists = db.playlists
db_lyrics = db.lyrics

headers = {
    'Cookie': 'appver=1.5.0.75771',
    'Referer':'http://music.163.com/'
}

def search(keywords):
	url = 'http://music.163.com/api/search/pc'
	data = {'s': keywords, 'offset': 1, 'limit': 10, 'type': 1000}
	req = requests.post(url, data=data, headers=headers)
	content = req.json()
	playlists = []
	for item in content['result']['playlists']:
		try:
			playlists.append(item['id'])
		except Exception as e:
			print(e)
			continue
	return playlists

# 根据歌单 ID, 获取所歌单内歌曲信息，保存到数据库
def get_songs(ply_lists):
    url = 'http://music.163.com/api/playlist/detail?id={}&updateTime=-1'
    for id in ply_lists:
        print('正在采集歌曲:',id)
        s_url = url.format(id)
        req = requests.get(s_url,headers=headers)
        content = req.json()
        db_playlists.insert_one(content['result'])

# 获取歌词
def get_lyric():
	url = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'
	for playlist in db_playlists.find():
		for track in playlist['tracks']:
			song_id = track['id']
			l_url = url.format(song_id)
			print('正在处理:',l_url)
			req = requests.get(l_url,headers=headers)
			content = req.json()
			db_lyrics.update_one({'id': song_id},{'$set': content},upsert=True)

def main():
	ply_lists = search('程序员')
	get_songs(ply_lists)
	get_lyric()

if __name__ == '__main__':
	main()







