import requests
import re
import os
import time


def fetch_html_text(fetch_url):
    # 模拟浏览器
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(fetch_url, headers=headers)
    response.encoding = 'gbk'
    response_html = response.text
    response.close()
    return response_html


def overwrite_dir(in_title):
    clsq = "pyfkclsq"
    my_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + os.path.sep + clsq + os.path.sep + in_title
    print(my_path)
    if os.path.exists(my_path):
        os.rmdir(my_path)
    os.makedirs(my_path)
    return my_path


# start program
endpoint = "https://cl.ee87.xyz/"
url = endpoint + "thread0806.php?fid=7"
responseText = fetch_html_text(url)
result = re.findall('<td class="tal" id="">\\s+?<h3><a href="(.+?)" target="_blank" id="">(.+?)</a></h3>',
                    responseText)
print(len(result))
for link in result:
    title = link[1]
    detailUrl = endpoint + link[0]
    biz_path = overwrite_dir(title)
    detail_text = fetch_html_text(detailUrl)
    print(detailUrl)
    file = open(biz_path + os.path.sep + title + ".html", "w")
    file.write(detail_text.replace("ess-data", "src"))
    file.close()
    time.sleep(60)
    break
