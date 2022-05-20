# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 获取出口ip.py
# Time       ：2022/5/20 10:09
# Author     ：man jia lian
# version    ：python 3.9
# Description：

# 通过 http://myip.ipip.net/ 获取到出口ip
"""

import re
import requests


def get_export_ip(ip="http://myip.ipip.net/") -> str:
    # 获取出口ip
    try:
        req = requests.get(ip).text
    except Exception:
        return False
    result = re.findall(r'\D(?:\d{1,3}\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\D', str(req))
    ret = re.search(r'((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)', str(result))

    # write Local_ip
    with open(f"./local_ip", 'w') as f:
        # f.write(bytes(b'test'))
        f.write(ret[0])
    return ret[0]


if __name__ == '__main__':
    print(get_export_ip())

