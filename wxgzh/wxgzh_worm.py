import os.path

import htmlUtil
from bs4 import BeautifulSoup
import wkhtmltopdf
import common

html_info = htmlUtil.fetch_html_info('https://mp.weixin.qq.com/s/jWK5LAYsJ5-aVTrBPealAg', 'utf-8')
html_soup = BeautifulSoup(html_info, features="html.parser")

courses = html_soup.select('#js_content > p > a')
for course in courses:
    print(course.text, )
    file_path = common.get_home_path() + os.path.sep + 'pdfs' + os.path.sep + 'abc.pdf'
    print(file_path)
    wkhtmltopdf(course['href'], file_path)
    break
