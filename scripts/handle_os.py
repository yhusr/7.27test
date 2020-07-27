# -*- coding:utf-8 -*-
# @Time    :2020-07-27 10:28
# @Author  :toy_yh
# @File    :handle_os.py
# @Software:PyCharm

import os
import time


# 获取当前文件路径
current_path = os.path.abspath(__file__)
scripts_path = os.path.dirname(current_path)
root_path = os.path.dirname(scripts_path)

# 获取config目录路径
config_path = os.path.join(root_path, 'config')
yaml_path = os.path.join(config_path, 'conf.yaml')

# 获取ini配置文件的路径
ini_path = os.path.join(config_path, 'ini_conf.ini')

# 获取data目录路径
data_path = os.path.join(root_path, 'data')
# 获取excel文件路径
excel_path = os.path.join(data_path, 'excelcases.xlsx')


# log文件夹路径
str_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
log_path = os.path.join(root_path, 'log')
work_log_path = os.path.join(log_path, str_time + 'log.log')