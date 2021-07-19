from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import htmlUtil
import common
import time
import os


def download_img_in_html(in_file_path):
    c_files = os.listdir(in_file_path)
    non_html_file_count = 0
    for c_file in c_files:
        if c_file.endswith('html'):
            c_file_path = in_file_path + os.path.sep + c_file
            html = open(c_file_path)
            html_info = html.read()
            html.close()
        else:
            non_html_file_count += 1
    html_soup = BeautifulSoup(html_info, features="html.parser")
    imgs = html_soup.findAll(lambda item: item.has_attr('iyl-data') and item.has_attr('ess-data'))
    print('html 一共包含： ', len(imgs), '张图片')
    print('已下载： ', non_html_file_count, '张图片')
    tasks = []
    if len(imgs) > non_html_file_count:
        for img in imgs:
            img_url = img['ess-data']
            img_path = in_file_path + os.path.sep + common.get_name_from_url(img_url)
            tasks.append(pool.submit(htmlUtil.download_image, img_path, img_url))
    for task in tasks:
        if not task.done():
            time.sleep(10)
            break


pool = ThreadPoolExecutor(20, 'thread_name_prefix_')
index = 0
count = 10
home_path = common.get_home_path()
files = os.listdir(home_path)
files.sort(key=lambda item: os.path.getctime(common.get_home_path() + os.path.sep + item), reverse=True)
for file in files:
    file_path = home_path + os.path.sep + file.title()
    if not os.path.isfile(file_path):
        download_img_in_html(file_path)
        index += 1
        if index >= count:
            break
