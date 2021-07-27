import os.path

import htmlUtil
from bs4 import BeautifulSoup
import common
import pdfkit

html_info = htmlUtil.fetch_html_info('https://mp.weixin.qq.com/s/jWK5LAYsJ5-aVTrBPealAg', 'utf-8')
html_soup = BeautifulSoup(html_info, features="html.parser")
path_wk = r'D:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe'  # 安装位置
config = pdfkit.configuration(wkhtmltopdf=path_wk)
courses = html_soup.select('#js_content > p > a')
for course in courses:
    print(course.text, course['href'])
    file_path = common.get_home_path() + os.path.sep + 'pdfs' + os.path.sep + course.text + '.pdf'
    print(file_path)
    pdfkit.from_url(course['href'], file_path, configuration=config)
    break
