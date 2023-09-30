import random
import time

import requests
import os

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
]


def fetch_html_info(fetch_url, charset='utf-8'):
    response_html = ''
    try:
        # 模拟浏览器
        headers = {
            'accept': '*/*',
            'user-agent': random.choice(user_agents)
        }
        response = requests.get(fetch_url, timeout=3600, headers=headers)
        response.encoding = charset
        response_html = response.text
        response.close()
    except Exception as e:
        print(fetch_url, e)
    return response_html


def download_image(i_img_path, i_img_url):
    try:
        # 模拟浏览器
        headers = {
            'accept': '*/*',
            "user-agent": random.choice(user_agents)
        }
        print(i_img_path, "是否已经存在: ", os.path.exists(i_img_path))
        if not os.path.exists(i_img_path):
            print(i_img_path, "开始下载")
            # 不存在，则下载
            data = requests.get(i_img_url, timeout=4500, headers=headers).content  # 获取图片的二进制格式
            with open(i_img_path, 'wb') as f:
                f.write(data)
                f.flush()
            f.close()
            return True
        else:
            print(i_img_path, "已经存在无需下载")
            return False
    except Exception as e:
        print(i_img_path, i_img_url, 'download got error', e)
    finally:
        return False


def get_redirect_urls(i_img_path, i_img_url):
    headers = {
        "user-agent": random.choice(user_agents),
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    red_urls = requests.get(i_img_url, timeout=60000, headers=headers)
    print("red_urls1")
    print(red_urls)
    print("red_urls2")
