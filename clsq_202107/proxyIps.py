# http://www.kxdaili.com/dailiip.html
# encoding = utf8
import requests
from bs4 import BeautifulSoup
import urllib
import socket

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent


def fetch_html_text(fetch_url):
    # 模拟浏览器
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(fetch_url, headers=headers)
    response.encoding = 'utf-8'
    response_html = response.text
    response.close()
    return response_html


'''
获取所有代理IP地址
'''


def getProxyIp():
    proxy = []
    url = 'http://www.kxdaili.com/dailiip/1/1.html'
    res = fetch_html_text(url)
    soup = BeautifulSoup(res)
    ips = soup.findAll('tr')
    for x in range(1, len(ips)):
        ip = ips[x]
        tds = ip.findAll("td")
        ip_temp = tds[1].contents[0] + "\t" + tds[2].contents[0]
        proxy.append(ip_temp)
    return proxy


'''
验证获得的代理IP地址是否可用
'''


def validateIp(proxy):
    url = "http://ip.chinaz.com/getip.aspx"
    f = open("E:\ip.txt", "w")
    socket.setdefaulttimeout(3)
    for i in range(0, len(proxy)):
        try:
            ip = proxy[i].strip().split("\t")
            proxy_host = "http://" + ip[0] + ":" + ip[1]
            proxy_temp = {"http": proxy_host}
            res = urllib.urlopen(url, proxies=proxy_temp).read()
            f.write(proxy[i] + '\n')
            print(proxy[i])
        except Exception as e:
            continue
    f.close()


proxy = getProxyIp()
