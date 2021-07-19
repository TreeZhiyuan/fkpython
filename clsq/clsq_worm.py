import common
import htmlUtil
from bs4 import BeautifulSoup

# start program
pageCount = 1
endpoint = 'https://cl.ee87.xyz/'
pageNo = 1
while pageNo <= pageCount:
    url = endpoint + 'thread0806.php?fid=7&page=' + str(pageNo)
    html_info = htmlUtil.fetch_html_info(url)
    soup = BeautifulSoup(html_info, features='html.parser')
    aTags = soup.select('#tbody > tr > td > h3 > a')
    txtFilepath = common.get_title_txt_file_path(str(pageNo))
    datas = []
    for tag in aTags:
        tagUrl = endpoint + tag['href']
        tagTitle = tag.text[:61]
        datas.append(tagUrl + " " + tagTitle)
    common.write_file_info(txtFilepath, datas)
    pageNo += 1
