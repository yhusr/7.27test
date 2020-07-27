# -*- coding:utf-8 -*-
# @Time    :2020-07-27 8:56
# @Author  :toy_yh
# @File    :run.py.py
# @Software:PyCharm
import pytest


if __name__ == '__main__':
    pytest.main(["--reruns", "2", "--reruns-delay", "5", "--junitxml=reports/allure.xml"])
