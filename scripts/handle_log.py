# -*- coding:utf-8 -*-
# @Time    :2020-07-27 13:31
# @Author  :toy_yh
# @File    :handle_log.py
# @Software:PyCharm
import logging
from scripts.handle_os import work_log_path


class HandleLog:

    @classmethod
    def get_logger(cls):
        logger = logging.getLogger('interface_test')
        logger.setLevel('DEBUG')
        format_log = logging.Formatter('%(asctime)s - %(name)s - '
                                       '[%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')

        # 控制台输出
        sh = logging.StreamHandler()
        sh.setLevel('DEBUG')
        sh.setFormatter(format_log)
        logger.addHandler(sh)

        # 文件输出
        fh = logging.FileHandler(filename=work_log_path, encoding='utf-8')
        fh.setFormatter(format_log)
        fh.setLevel('DEBUG')
        logger.addHandler(fh)

        return logger


hl = HandleLog.get_logger()
