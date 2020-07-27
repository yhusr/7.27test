# -*- coding:utf-8 -*-
# @Time    :2020-07-27 14:35
# @Author  :toy_yh
# @File    :conftest.py.py
# @Software:PyCharm
import pytest

from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql
from scripts.handle_conf import hy


@pytest.fixture()
def set_up():
    hr = HandleRequest()
    hm = HandleMysql()
    hr.common_head(hy.read_yaml('api', 'header'))
    yield hr, hm
    hr.close()
    hm.close()
