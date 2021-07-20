import os
import random
import re
from bs4 import BeautifulSoup
import common
import htmlUtil
import time

go = False
if go:
    clsq = "pyfkclsq"
    my_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + os.path.sep + clsq
    print(my_path)
    if not os.path.exists(my_path):
        os.mkdir(my_path)
    tagUrl = 'https://cl.ee87.xyz/' + '/htm_data/2106/7/4536996.html'
    if "?" in tagUrl:
        print('没得玩', tagUrl)
    else:
        print('有得玩', tagUrl)
    html_path = 'C:\\Users\\86177\\Desktop\\77.html'
    file = open(html_path)
    html_info = file.read()
    soup = BeautifulSoup(html_info, features="html.parser")
    titles = soup.select("#tbody > tr > td > h3 > a")
    file = open(file="tie.txt", mode="w+", encoding="utf-8")
    for title in titles:
        file.writelines(title['href'] + " " + title.text + "\n")
    print(file.read())
    file.close()
# https://cl.ee87.xyz/read.php?tid=4593740 [搞笑GIF段子]姑娘，你是干嘛了，膝盖受这么重的伤
# https://cl.ee87.xyz/htm_data/2107/7/4596293.html 有种诱惑，叫低腰裤[ 80P]

print('a b c'.split(' ', 1)[1])
print(common.get_name_from_url('https://x6img.com/i/2021/07/12/vnknlo.gif'))

# print(htmlUtil.fetch_html_info('https://cl.ee87.xyz/htm_data/2106/7/4547021.html'))
print(time.strftime("%Y-%m-%d%H:%M:%S", time.localtime()))
home_path = common.get_home_path()
files1 = os.listdir(home_path)
files1.sort(key=lambda path1: time.ctime(os.path.getmtime(common.get_home_path() + os.path.sep + path1)))
print(files1)
for item in files1:
    print(time.ctime(os.path.getmtime(common.get_home_path() + os.path.sep + item)))
