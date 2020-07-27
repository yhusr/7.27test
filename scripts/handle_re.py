# -*- coding:utf-8 -*-
# @Time    :2020-07-27 13:58
# @Author  :toy_yh
# @File    :handle_re.py
# @Software:PyCharm
import re
from scripts.handle_mysql import HandleMysql


class HandleRe:

    @classmethod
    def my_re(cls, datas):
        hm = HandleMysql()
        phone = hm.get_non_existent()
        if re.search(r'{no_exist_phone}', datas):
            result = re.sub(r'{no_exist_phone}', phone, datas)
            return result
        return datas
