# -*- coding:utf-8 -*-
# @Time    :2020-07-27 13:45
# @Author  :toy_yh
# @File    :test_register_case.py
# @Software:PyCharm
import unittest
from lib.ddt import ddt, data

from scripts.handle_excel import HandleExcel
from scripts.handle_conf import hy
from scripts.handle_re import HandleRe
from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql
from scripts.handle_log import hl


@ddt
class TestRegisterCase(unittest.TestCase):
    he = HandleExcel(sheetname='register')
    obj_li = he.read_excel()

    @classmethod
    def setUpClass(cls):
        cls.hr = HandleRequest()
        cls.hm = HandleMysql()
        cls.hr.common_head(hy.read_yaml('api', 'header'))

    @data(*obj_li)
    def test_register(self, obj):
        title = obj.title
        base_url = hy.read_yaml('api', 'load')
        test_url = obj.url
        all_url = ''.join((base_url, test_url))
        right_data = HandleRe.my_re(datas=obj.data)
        result = self.hr.send(url=all_url, data=right_data)
        try:
            self.assertListEqual([result.json()['code'], result.json()['msg']], [obj.expected, obj.msg], msg=f'用例{title}执行完成')
            if obj.caseId == 1:
                my_data = eval(right_data)
                bl = self.hm.mysql_exist(sql=hy.read_yaml('mysql', 'phone_sql'), args=my_data['mobile_phone'])
                self.assertTrue(expr=bl)
        except Exception as e:
            self.he.write_excel(row_num=int(obj.caseId)+1, col_num=7, value='fail')
            self.he.write_excel(row_num=int(obj.caseId)+1, col_num=8, value=result.text)
            hl.error(e)
            raise e
        else:
            self.he.write_excel(row_num=int(obj.caseId) + 1, col_num=7, value='success')
            self.he.write_excel(row_num=int(obj.caseId) + 1, col_num=8, value=result.text)
            hl.info(obj.title)

    @classmethod
    def tearDownClass(cls):
        cls.hr.close()
        cls.hm.close()


