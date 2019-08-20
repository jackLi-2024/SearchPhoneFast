#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import sys
import json

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass

import grequests


def crawler(filename=None):
    requests_list = []
    with open(filename, "r") as f:
        content = f.read()
    urls = json.loads(content)
    for one in urls:
        requests_list.append(grequests.get(one, timeout=1))

    response_list = grequests.map(requests_list)
    with open(filename, "w") as f:
        for one in response_list:
            try:
                f.write(json.dumps(one.json())+ "\n")
            except:
                pass


if __name__ == '__main__':
    # urls = []
    # for one in range(10):
    #     urls.append("http://opendata.baidu.com/api.php?resource_name=guishudi&query=18404983792")
    filename = sys.argv[1]
    crawler(filename)
