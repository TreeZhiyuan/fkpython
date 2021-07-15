import base64

import requests
import re
import os
import time
import random
from bs4 import BeautifulSoup


def fetch_html_info(fetch_url):
    # 模拟浏览器
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]
    headers = {
        "user-agent": user_agents[random.randint(0, len(user_agents) - 1)]
    }
    print(headers)
    response = requests.get(fetch_url, headers=headers)
    response.encoding = 'gbk'
    response_html = response.text
    response.close()
    return response_html


def filename_filter(filename):
    filename = re.sub('[\\/:*?"<>|\\.]', '', filename)
    return filename


def overwrite_dir(in_title):
    in_title = filename_filter(in_title)
    clsq = "pyfkclsq"
    my_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + os.path.sep + clsq + os.path.sep + in_title
    if not os.path.exists(my_path):
        os.makedirs(my_path)
    return my_path


html_info = ''
result = re.findalla1('<td class="tal" id="">\\s+?<h3><a href="(.+?)" target="_blank" id="">(.+?)</a></h3>',
                      html_info)
endpoint = "https://cl.ee87.xyz/"
print(len(result))
for link in result:
    title = link[1]
    detailUrl = endpoint + link[0]
    biz_path = overwrite_dir(title)
    detail_text = fetch_html_info(detailUrl)
    print(detailUrl)
    file = open(biz_path + os.path.sep + str(hash(title)) + ".html", "w")
    file.write(detail_text)
    file.close()
    time.sleep(15)
