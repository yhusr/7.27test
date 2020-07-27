# -*- coding:utf-8 -*-
# @Time    :2020-07-27 8:58
# @Author  :toy_yh
# @File    :handle_excel.py
# @Software:PyCharm

import openpyxl

from scripts.handle_os import excel_path

class ObjExcel:
    pass


class HandleExcel:
    def __init__(self, sheetname,filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = excel_path

        self.sheetname = sheetname

    def open_excel(self):
        self.shbook = openpyxl.load_workbook(self.filepath)
        self.sh = self.shbook[self.sheetname]

    def read_excel(self):
        """
        此方法用于处理读取excel中数据
        :return:
        """
        self.open_excel()
        ex_value = list(self.sh.rows)
        head_li = [h.value for h in ex_value[0]]
        obj_li = []
        for v in ex_value[1:]:
            eo = ObjExcel()
            value_li = [vl.value for vl in v]
            my_zip = zip(head_li, value_li)
            for mz in my_zip:
                setattr(eo, mz[0], mz[1])
            obj_li.append(eo)
        self.shbook.close()
        return obj_li

    def write_excel(self, row_num, col_num, value):
        self.open_excel()
        self.sh.cell(row=row_num, column=col_num, value=value)
        self.shbook.save(self.filepath)
        self.shbook.close()


if __name__ == '__main__':
    he = HandleExcel('register')
    obj_li = he.read_excel()
    print(obj_li)
    print(obj_li[1].data)