import common
import htmlUtil
from bs4 import BeautifulSoup

# start program
count = 32
index = 0
endpoint = 'https://cl.1538x.xyz/'
pageNo = 1

txtFilepath = common.get_title_txt_file_path_hsxs()
common.remove_file(txtFilepath)
while index <= count:
    url = endpoint + 'thread0806.php?fid=20&page=' + str(pageNo)
    html_info = htmlUtil.fetch_html_info(url)
    soup = BeautifulSoup(html_info, features='html.parser')
    aTags = soup.select('#tbody > tr > td.tal > h3 > a')
    datas = []
    for tag in aTags:
        tagUrl = endpoint + tag['href']
        tagTitle = tag.text
        datas.append(tagUrl + " " + tagTitle)
    common.write_file_info_append(txtFilepath, datas)
    pageNo += 1
    index += 1
