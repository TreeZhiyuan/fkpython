import common
import os
from bs4 import BeautifulSoup
import time
import htmlUtil


def download_img_in_html(in_file_path):
    print(in_file_path)
    c_files = os.listdir(in_file_path)
    for c_file in c_files:
        if c_file.endswith('html'):
            c_file_path = in_file_path + os.path.sep + c_file
            html = open(c_file_path)
            print(c_file_path)
            html_info = html.read()
            html.close()
            html_soup = BeautifulSoup(html_info, features="html.parser")
            imgs = html_soup.findAll(lambda item: item.has_attr('iyl-data') and item.has_attr('ess-data'))
            print('一共： ', len(imgs), '图片')
            for img in imgs:
                if htmlUtil.download_image(in_file_path, img['ess-data']):
                    time.sleep(10)


index = 0
count = 10
home_path = common.get_home_path()
files = os.listdir(home_path)
for file in files:
    file_path = home_path + os.path.sep + file.title()
    if not os.path.isfile(file_path):
        download_img_in_html(file_path)
        index += 1
        if index >= count:
            break
