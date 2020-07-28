# -*- coding:utf-8 -*-
# @Time    :2020-07-27 9:32
# @Author  :toy_yh
# @File    :handle_conf.py
# @Software:PyCharm
import yaml
import configparser

from scripts.handle_os import yaml_path, ini_path


class HandleYaml:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = yaml_path

    def read_yaml(self, section_name, option_name):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            st = yaml.full_load(stream=f)
        result = st[section_name][option_name]
        return result

    def write_yaml(self, data, mode='a'):
        with open(self.filepath, mode=mode, encoding='utf-8') as f:
            yaml.dump(data, stream=f, allow_unicode=True)


hy = HandleYaml()



class HandleIni:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = ini_path
        self.conf = configparser.ConfigParser()

    def read_ini(self, section_name, option_name):
        self.conf.read(self.filepath, encoding='utf-8')
        result = self.conf.get(section=section_name, option=option_name)
        return result

    def write_ini(self, datas):
        for data in datas:
            self.conf[data] = datas[data]
        with open(self.filepath, 'a', encoding='utf-8') as f:
            self.conf.write(f)


if __name__ == '__main__':
    # hy = HandleYaml()
    # my_name = hy.read_yaml('excel', 'name')
    # print(my_name)
    hi = HandleIni()
    result = hi.read_ini('excel', 'name')
    print(result)