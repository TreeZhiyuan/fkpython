# encoding = utf8
import os
import random
import re
import requests
from bs4 import BeautifulSoup


def get_name_from_url(url):
    sps = url.rsplit("/", 1)
    return sps[-1]


def download_image(img_url):
    print(img_url)
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]
    # 模拟浏览器
    headers = {
        "user-agent": user_agents[random.randint(0, len(user_agents) - 1)]
    }
    print(headers["user-agent"])
    data = requests.get(img_url, headers=headers).content  # 获取图片的二进制格式
    img_path = 'D:\\atp_workspace\\pyfkclsq\\2021\\' + get_name_from_url(img_url)
    if not os.path.exists(img_path):
        with open(img_path, 'wb') as f:
            f.write(data)
            f.flush()
        f.close()
        return True
    else:
        return False


html_path = 'C:\\Users\\86177\\Desktop\\77.html'
file = open(html_path)
html_info = file.read()
titles = re.findall('<td class="tal" id="">\\s+?<h3><a href="(.+?)" target="_blank" id="">(.+?)</a></h3>', html_info)
soup = BeautifulSoup(html_info, features="html.parser")
titles = soup.select("#tbody > tr > td > h3 > a")
print(len(titles))
for title in titles:
    print(title['href'], title.text[:57])
# soup = BeautifulSoup(html_info, features="html.parser")
# links = soup.findAll("link")
# for link in links:
#     href = link["href"]
#     if not href.startswith('http'):
#         link["href"] = "https:" + href
# scripts = soup.findAll(lambda tag: tag.has_attr('src') and tag.name == 'script')
# for script in scripts:
#     src = script["src"]
#     if not src.startswith('http'):
#         script["src"] = "https:" + src
# with open(html_path, "wb") as f_output:
#     f_output.write(soup.prettify("gbk"))

# imgs = soup.findAll(lambda tag: tag.has_attr('iyl-data') and tag.has_attr('ess-data') )
# for img in imgs:
#     print(img["src"])
