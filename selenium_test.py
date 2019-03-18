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


if __name__ == '__main__':
    main()
