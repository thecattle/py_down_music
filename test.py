# from urllib import request

import requests

if __name__ == '__main__':
  # url = "http://m10.music.126.net/20190316041902/35a2108930c868a08fb46b077b6b9af2/ymusic/525d/540b/510f/e7403c0f89ca574eea7dfea2ac7601f5.mp3"
  # url = 'http://music.163.com/song/media/outer/url?id=1336856777.mp3'
  url = 'https://music.163.com/#/playlist?id=2593304089'
  path = '我曾.mp3'
  user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
  headers = {'User-Agent':user_agent,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Upgrade-Insecure-Requests':'1'}
  response = requests.get(url,headers=headers)
  response.encoding = 'utf-8'
  html = response.text
  print(html)
  # with open(path, 'wb') as f:
  #   f.write(response.content)
  #   f.flush()
  # request.urlretrieve(url, path)
  print('下载完成')