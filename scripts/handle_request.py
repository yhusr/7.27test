# -*- coding:utf-8 -*-
# @Time    :2020-07-27 11:01
# @Author  :toy_yh
# @File    :handle_request.py
# @Software:PyCharm
import requests
import json


class HandleRequest:
    def __init__(self):
        self.one_session = requests.session()

    def common_head(self,heads):
        self.one_session.headers.update(heads)

    def send(self, url, method='post', data=None, is_json=True, **kwargs):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                data = eval(data)
        method = method.lower()

        if method == 'get':
            result = self.one_session.request(method=method, url=url, params=data, **kwargs)
        elif method in ('post', 'patch', 'put', 'delete'):
            if is_json:
                result = self.one_session.request(method=method, url=url, json=data, **kwargs)
            else:
                result = self.one_session.request(method=method, url=url, data=data, **kwargs)
        else:
            result = None
            print(f'此方法{method}不存在')
        return result

    def close(self):
        self.one_session.close()

