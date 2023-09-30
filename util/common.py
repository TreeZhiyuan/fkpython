import re
import os

'''
windows环境创建目录不允许部分特殊字符
将传入目录名称进行合规化操作
'''


def filename_filter(filename):
    filename = re.sub('[/:*?"<>| .\\n]', '', filename)
    return filename


'''
根据传入的url获取图片的名称
'''


def get_name_from_url(in_url):
    sps = in_url.rsplit("/", 1)
    name = sps[-1]
    return name


def get_img_name_from_url(in_url):
    name = get_name_from_url(in_url)
    if "." in name:
        return name
    else:
        return name + ".jpg"


'''
社区爬虫的base目录
'''


def get_home_path():
    clsq = "pyfkclsq"
    return os.path.abspath(os.path.join(os.getcwd(), "../..")) + os.path.sep + clsq


'''
社区爬虫标题目录
'''


def get_item_path(title):
    return get_home_path() + os.path.sep + filename_filter(title)


def get_title_txt_file_path(pageNo):
    return get_home_path() + os.path.sep + 'clsp_titles_' + pageNo + '.txt'


def get_title_txt_file_path_hsxs():
    return get_home_path() + os.path.sep + 'clsp_titles_wx.txt'


def write_file_info(file_path, datas):
    file = open(file=file_path, mode='w+', encoding='utf-8')
    for data in datas:
        file.writelines(data + "\n")
    file.close()


def write_file_info_append(file_path, datas):
    file = open(file=file_path, mode='a', encoding='utf-8')
    for data in datas:
        file.writelines(data + "\n")
    file.close()


def remove_file(file_path):
    os.remove(file_path)