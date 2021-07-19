import random
import requests
import common
import os

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
]


def fetch_html_info(fetch_url):
    response_html = ''
    try:
        # 模拟浏览器
        headers = {
            "user-agent": user_agents[random.randint(0, len(user_agents) - 1)]
        }
        response = requests.get(fetch_url, timeout=20, headers=headers)
        response.encoding = 'gbk'
        response_html = response.text
        response.close()
    except Exception as e:
        print(fetch_url, e)
    return response_html


def download_image(i_img_path, i_img_url):
    try:
        # 模拟浏览器
        headers = {
            "user-agent": user_agents[random.randint(0, len(user_agents) - 1)]
        }
        if not os.path.exists(i_img_path):
            # 不存在，则下载
            data = requests.get(i_img_url, timeout=20, headers=headers).content  # 获取图片的二进制格式
            with open(i_img_path, 'wb') as f:
                f.write(data)
                f.flush()
            f.close()
            return True
        else:
            return False
    except Exception as e:
        print(i_img_path, e)
    finally:
        return False
