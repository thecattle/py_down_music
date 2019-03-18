#encoding: utf-8
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def main():
  browser = webdriver.Chrome()
  # browser.get("https://music.163.com/#/playlist?id=2593304089")
  browser.get("https://music.163.com/#/discover/toplist?id=3778678")
  browser.switch_to.frame('contentFrame')

  soup = BeautifulSoup(browser.page_source,'lxml')
  # print(browser.page_source)
  find_list  = soup.find('tbody').find_all('a')
  for a in find_list:
    b=a.find('b')
    if b is not None:
      song=a.get("href")
      name=b.get("title")
      print("%s,%s"%(song,name))
      try:
        down(song,name)
        print()
      except Exception as e:
        print(e)
      time.sleep(1)

def down(song,name):
  id=song.split("=")[1]
  name=name.replace("/","|")
  url = 'http://music.163.com/song/media/outer/url?id='+id+'.mp3'
  path = './music2/'+str(name)+'.mp3'
  user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
  headers = {'User-Agent':user_agent,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Upgrade-Insecure-Requests':'1'}
  response = requests.get(url,headers=headers)
  # response.encoding = 'utf-8'
  # html = response.text
  # print(html)
  with open(path, 'wb') as f:
    f.write(response.content)
    f.flush()
  print(name+' 下载完成')

if __name__ == '__main__':
  main()
