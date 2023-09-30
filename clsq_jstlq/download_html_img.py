import random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import htmlUtil
import common
import time
import os


def download_img_in_html(in_file_path):
    c_files = os.listdir(in_file_path)
    non_html_file_count = 0
    html_file_path = ''
    for c_file in c_files:
        if c_file.endswith('html'):
            html_file_path = in_file_path + os.path.sep + c_file
        else:
            non_html_file_count += 1
    if len(html_file_path) == 0 or os.path.getsize(html_file_path) == 0:
        print(in_file_path, '>>>>>>>>>>>>> no html file found or html is empty')
    else:
        html = open(html_file_path)
        html_info = html.read()
        html.close()
        html_soup = BeautifulSoup(html_info, features="html.parser")
        imgs = html_soup.findAll(lambda item: item.has_attr('iyl-data') and item.has_attr('ess-data'))
        print(in_file_path, ': html 一共包含', len(imgs), '张图片')
        print(',已下载', non_html_file_count, '张图片')
        tasks = []
        if len(imgs) > non_html_file_count:
            for img in imgs:
                img_url = img['ess-data']
                img_path = in_file_path + os.path.sep + common.get_name_from_url(img_url)
                htmlUtil.download_image(img_path, img_url)
                time.sleep(random.random() * 60)


specific = False
pool = ThreadPoolExecutor(25, 'thread_name_prefix_')
if not specific:
    index = 0
    count = 10
    home_path = common.get_home_path() + os.path.sep + 'posts'
    files = os.listdir(home_path)
    files.sort(key=lambda item: os.path.getctime(common.get_home_path() + os.path.sep + 'posts' + os.path.sep + item),
               reverse=True)
    for file in files:
        file_path = home_path + os.path.sep + file.title()
        if not os.path.isfile(file_path):
            download_img_in_html(file_path)
            index += 1
            if index >= count:
                break
else:
    const_path = 'D:\\atp_workspace\\pyfkclsq'
    _file_path = const_path + os.path.sep + ''
    download_img_in_html(_file_path)
