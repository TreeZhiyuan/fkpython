import os
import random
import re
from bs4 import BeautifulSoup


def filename_filter(filename):
    filename = re.sub('[\\/:*?"<>|\\.]', '', filename)
    return filename


def get_name_from_url(in_url):
    sps = in_url.rsplit("/", 1)
    name = filename_filter(sps[-1])
    if "." in name:
        return name
    else:
        return name + ".jpg"


go = False
if go:
    clsq = "pyfkclsq"
    my_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + os.path.sep + clsq
    print(my_path)
    if not os.path.exists(my_path):
        os.mkdir(my_path)
    print(random.randint(0, 1))
    print(hash("dwadwa"))
    print(filename_filter("dwadw:dwdd.."))
    print("1234"[:6])
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
print(titles)
file = open(file="tie.txt", mode="w+", encoding="utf-8")
for title in titles:
    file.writelines(title['href'] + " " + title.text+"\n")

file.close()
