import htmlUtil
import common
import os
from bs4 import BeautifulSoup


def get_txt_file_paths():
    paths = []
    home_path = common.get_home_path()
    files = os.listdir(home_path)
    for file in files:
        txt_file_path = home_path + os.path.sep + file.title()
        if os.path.isfile(txt_file_path):
            paths.append(txt_file_path)
    return paths


def get_txt_file_content(txtFilePath):
    contents = []
    file = open(txtFilePath, 'r', encoding="utf-8")
    for line in file.readlines():
        contents.append(line)
    return contents


def download_html_infos(d_html_url, d_html_path):
    item_html_info = htmlUtil.fetch_html_info(d_html_url)
    print(item_html_info)
    item_soup = BeautifulSoup(item_html_info, features="html.parser")
    links = item_soup.findAll("link")
    for link in links:
        href = link["href"]
        if not href.startswith('http'):
            link["href"] = "https:" + href
    scripts = item_soup.findAll(lambda soup_tag: soup_tag.has_attr('src') and soup_tag.name == 'script')
    for script in scripts:
        src = script["src"]
        if not src.startswith('http'):
            script["src"] = "https:" + src
    with open(d_html_path, "wb") as f_output:
        f_output.write(item_soup.prettify("gbk"))
    f_output.close()


for path in get_txt_file_paths():
    for txt in get_txt_file_content(path):
        print(txt)
        a = txt.split(' ', 1)
        html_url = a[0]
        if '?' in html_url:
            print(html_url)
        else:
            html_name = common.get_name_from_url(html_url)
            file_name = common.filename_filter(a[1][:61])
            my_tag_path = common.get_home_path() + os.path.sep + file_name
            if not os.path.exists(my_tag_path):
                os.makedirs(my_tag_path)
            html_path = my_tag_path + os.path.sep + html_name
            if os.path.exists(html_path):
                print('already exists')
            else:
                download_html_infos(html_url, html_path)
