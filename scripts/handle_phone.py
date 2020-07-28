# -*- coding:utf-8 -*-
# @Time    :2020-07-28 13:17
# @Author  :toy_yh
# @File    :handle_phone.py
# @Software:PyCharm
import os

from scripts.handle_request import HandleRequest
from scripts.handle_conf import hy, HandleYaml
from scripts.handle_mysql import HandleMysql
from scripts.handle_os import config_path


class HandlePhone:

    @classmethod
    def get_phone(cls, username, password='123456678', type=1):
        hr = HandleRequest()
        hm = HandleMysql()
        base_url = hy.read_yaml('api', 'load')
        register_url = hy.read_yaml('api', 'register')
        all_url = ''.join((base_url, register_url))
        while True:
            phone = hm.get_non_existent()
            data = {
                "mobile_phone": phone,
                "pwd": password,
                "type": type,
                "reg_name": username
            }
            hr.common_head(hy.read_yaml('api', 'header'))
            result = hr.send(url=all_url, data=data)
            if result.json()['code'] == 0 and result.json()['msg'] == 'OK':
                break
        user_id = hm.get_mysql_result(sql=hy.read_yaml('mysql', 'user_id'), args=phone)
        result_data = {
            username: {
                "mobilephone": phone,
                "pwd": password,
                "user_id": user_id[0]['id'],
                "reg_name": username
            }
        }
        hr.close()
        hm.close()
        return result_data

    @classmethod
    def generate_phone(cls):
        my_data = {}
        generate_phone_path = os.path.join(config_path, hy.read_yaml('api', 'phonePath'))
        my_yaml = HandleYaml(filepath=generate_phone_path)
        admin_result = cls.get_phone(username='admin', type=0)
        my_data.update(admin_result)
        invest_result = cls.get_phone(username='investor')
        my_data.update(invest_result)
        loan_result = cls.get_phone(username='loan')
        my_data.update(loan_result)
        my_yaml.write_yaml(data=my_data, mode='w')


if __name__ == '__main__':
    HandlePhone.generate_phone()


