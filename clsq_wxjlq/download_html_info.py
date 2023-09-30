import os
import common
import htmlUtil
from bs4 import BeautifulSoup


def get_txt_file_paths():
    paths = []
    home_path = common.get_home_path()
    files = os.listdir(home_path)
    for file in files:
        txt_file_path = home_path + os.path.sep + file.title()
        if os.path.isfile(txt_file_path):
            paths.append(txt_file_path)
    print('get_txt_file_paths', paths)
    return paths


def get_txt_file_content(txtFilePath):
    contents = []
    file = open(txtFilePath, 'r', encoding="utf-8")
    for line in file.readlines():
        contents.append(line)
    return contents


def download_html_infos(d_html_url, d_html_path):
    if os.path.exists(d_html_path) and os.path.getsize(html_path) > 0:
        print(d_html_path, d_html_url, 'already exists')
    else:
        print(d_html_path, d_html_url, '需要下载的html')
        item_html_info = htmlUtil.fetch_html_info(d_html_url)
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
            f_output.flush()
        f_output.close()


download_text_path = common.get_home_path() + os.path.sep + 'download_hsxs.txt'
for txt in get_txt_file_content(download_text_path):
    a = txt.split(' ', 1)
    html_url = a[0]

    file_name = common.filename_filter(a[1][:61])
    my_tag_path = common.get_home_path() + os.path.sep + file_name
    if not os.path.exists(my_tag_path):
        os.makedirs(my_tag_path)
    if '?' in html_url:
        _html_info = htmlUtil.fetch_html_info(html_url)
        soup = BeautifulSoup(_html_info, features="html.parser")
        meta = soup.findAll(lambda _item: _item.has_attr('href') and _item.name == 'a')
        if len(meta) == 2:
            _endpoint = meta[0]
            target = meta[(len(meta) - 1)]
            _html_url = _endpoint['href'] + '/' + target['href']
            html_name = common.get_name_from_url(_html_url)
            html_path = my_tag_path + os.path.sep + 'novels' + os.path.sep + html_name
            download_html_infos(_html_url, html_path)
        else:
            print('解析失败', html_url)

    else:
        html_name = common.get_name_from_url(html_url)
        html_path = my_tag_path + os.path.sep + 'novels' + os.path.sep + html_name
        download_html_infos(html_url, html_path)
