# encoding: utf-8  
# @time: 2020/7/7 9:31 下午
# @author: hyt
# @contact: 2621498918@qq.com

import requests
def c():
    d = {
        'name': 'tom',
        'age': 20
    }
    response = requests.get('http://httpbin.org/get', params=d)
    print(response.text)
c()


