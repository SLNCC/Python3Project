# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import requests, os, webbrowser, bs4

url = 'http://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd
while not url.endswith('#'):

    #1.加载页面
    print("Downloadingpage %s...."%url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    #2.找到漫画图片的URL
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # 3.下载图片
        print("Downloadingimage %s...." % comicUrl)
        res =  requests.get(comicUrl)
        res.raise_for_status()
        # 4.保存图片./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #5. Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')


