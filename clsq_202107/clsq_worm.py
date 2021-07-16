import time

import requests
import re
import os
import random
from bs4 import BeautifulSoup

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]


def get_home_path():
    clsq = "pyfkclsq"
    home_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + os.path.sep + clsq
    return home_path


def fetch_html_info(fetch_url):
    # 模拟浏览器
    headers = {
        "user-agent": user_agents[random.randint(0, len(user_agents) - 1)]
    }
    response = requests.get(fetch_url, headers=headers)
    response.encoding = 'gbk'
    response_html = response.text
    response.close()
    return response_html


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


def overwrite_dir(in_title):
    in_title = filename_filter(in_title)
    my_path = get_home_path() + os.path.sep + in_title
    if not os.path.exists(my_path):
        os.makedirs(my_path)
    return my_path


def download_image(parent_path, img_url):
    # 模拟浏览器
    headers = {
        "user-agent": user_agents[random.randint(0, len(user_agents) - 1)]
    }
    data = requests.get(img_url, headers=headers).content  # 获取图片的二进制格式
    img_path = parent_path + os.path.sep + get_name_from_url(img_url)
    if not os.path.exists(img_path):
        with open(img_path, 'wb') as f:
            f.write(data)
            f.flush()
        f.close()
        return True
    else:
        return False


def do_item_opera(in_tagUrl, in_tagTitle):
    my_tag_path = get_home_path() + os.path.sep + filename_filter(in_tagTitle)
    print('my_tag_path: ', my_tag_path)
    if not os.path.exists(my_tag_path):
        os.makedirs(my_tag_path)
    item_html_info = fetch_html_info(in_tagUrl)
    file = open(my_tag_path + os.path.sep + str(hash(in_tagTitle)) + ".html", "w")
    item_soup = BeautifulSoup(item_html_info, features="html.parser")
    file.write(item_html_info)
    file.close()
    imgs = item_soup.findAll(lambda item: item.has_attr('iyl-data') and item.has_attr('ess-data'))
    print('一共： ', len(imgs), '图片')
    for img in imgs:
        if download_image(my_tag_path, img['ess-data']):
            time.sleep(20)


# start program
endpoint = "https://cl.ee87.xyz/"
url = endpoint + "thread0806.php?fid=7&page=1"
print(url)
html_info = fetch_html_info(url)
soup = BeautifulSoup(html_info, features="html.parser")
aTags = soup.select("#tbody > tr > td > h3 > a")
i = 0
skip = 0
for tag in aTags:
    tagUrl = endpoint + tag['href']
    tagTitle = tag.text[:61]
    if "?" in tagUrl:
        print('没得玩', tagUrl, tagTitle)
    else:
        i += 1
        do_item_opera(tagUrl, tagTitle)
        time.sleep(16)
    if i == 10:
        break
