#encoding: utf-8
import requests
import re
import json
import os

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}




def get_singermid():
  name = input('请输入你要下载歌曲的作者:')
  url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
  headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
  data = {
    'w': name,
    'jsonpCallback': 'MusicJsonCallback885332333726736', }
  response = requests.get(url, headers=headers, params=data).text
  patt = re.compile('MusicJsonCallback\d+\((.*?)\}\)')
  singermid = re.findall(patt, response)[0]
  singermid = singermid + '}'
  dic = json.loads(singermid)
  return dic['data']['song']['list'][0]['singer'][0]['mid']

#分页获取歌曲id
def music_down(singermid):
  url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg'
  num = 10
  begin = 0;
  total = 0;
  tag = True;
  while tag:
    params = {
      'g_tk': 5381,
      # 'jsonpCallback': 'MusicJsonCallbacksinger_track',
      'loginUin': 0,
      'hostUin': 0,
      'format': 'jsonp',
      'inCharset': 'utf8',
      'outCharset': 'utf-8',
      'notice': 0,
      'platform': 'yqq',
      'needNewCode': 0,
      'singermid': singermid,
      'order': 'listen',
      'begin': begin,  # 页数  0 30  60
      'num': num,
      'songstatus': 1,
    }
    response = requests.get(url, headers=headers, params=params)
    res = json.loads(response.text);
    total = res["data"]["total"];
    begin = begin+10;
    print("进度",(begin/total)*100)
    tag = (begin+num)<total;
    list_music_id(res["data"]["list"])
    # tag = False;
  print("over")

#获取每一页的歌曲id
def list_music_id(list):
  for i in list:
    name = i["musicData"]["songname"]
    songmid = i["musicData"]["songmid"]
    # print(name,songmid)
    # print(songmid)
    down(songmid)

#下载
def down(songId):
  headersDown ={'Accept':'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
                'Cache-Control':'no-cache',
                'Connection':'keep-alive',
                'Content-Length':'45',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Host':'music.sonimei.cn',
                'Origin':'http://music.sonimei.cn',
                'Pragma':'no-cache',
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'}


  data={'input':songId,'filter':'id','type':'qq','page':1}
  url="http://music.sonimei.cn"
  res=requests.post(url=url,data=data,headers=headersDown,timeout=30)
  res=json.loads(res.text)
  name=res["data"][0]["title"]+"-"+res["data"][0]["author"]
  url=res["data"][0]["url"]
  print("歌曲名称",name)
  print("下载链接",url)
  print(name + '下载中')

  music = requests.get(url, headers=headers).content
  with open('./music/' + name + '.mp3', 'wb') as f:
    f.write(music)
    f.close()
    print('下载完成《' + name + '》')
    print()

def main():
  # 获取 singermid
  # singermid = get_singermid()
  singermid = "0025NhlN2yWrP4"
  music_down(singermid)


if __name__ == '__main__':
  main()



