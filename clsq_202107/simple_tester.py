import base64
import os
import random
import re


def filename_filter(filename):
    filename = re.sub('[\\/:*?"<>|\\.]', '', filename)
    return filename


clsq = "pyfkclsq"
my_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + os.path.sep + clsq
print(my_path)
if not os.path.exists(my_path):
    os.mkdir(my_path)
print(random.randint(0, 1))
print(hash("dwadwa"))
print(filename_filter("dwadw:dwdd.."))
print("1234"[:6])
tagUrl = 'https://cl.ee87.xyz/' + '/htm_data/2106/7/4536996.html'
if "?" in tagUrl:
    print('没得玩', tagUrl)
else:
    print('有得玩', tagUrl)
