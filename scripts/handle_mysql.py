# -*- coding:utf-8 -*-
# @Time    :2020-07-27 11:38
# @Author  :toy_yh
# @File    :handle_mysql.py
# @Software:PyCharm
import pymysql
import random

from scripts.handle_conf import hy


class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host=hy.read_yaml('mysql', 'host'),
            user=hy.read_yaml('mysql', 'user'),
            password=hy.read_yaml('mysql', 'password'),
            port=hy.read_yaml('mysql', 'port'),
            db=hy.read_yaml('mysql', 'db'),
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def get_mysql_result(self, sql, args=None, is_more=True):
        self.cursor.execute(sql, args=args)
        self.conn.commit()
        if is_more:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()
        return result

    @classmethod
    def random_phone(cls):
        return hy.read_yaml('mysql', 'phone_pre') + str(''.join(random.sample('0123456789', 8)))

    def mysql_exist(self, sql, args):
        result = self.get_mysql_result(sql=sql, args=args)
        if result:
            return True
        else:
            return False

    def get_non_existent(self):
        sql = hy.read_yaml('mysql', 'phone_sql')
        while True:
            phone = self.random_phone()
            bl = self.mysql_exist(sql=sql, args=phone)
            if not bl:
                break
        return phone

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    hm = HandleMysql()
    phone = hm.get_non_existent()
    print(phone)


