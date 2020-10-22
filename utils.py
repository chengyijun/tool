# -*- coding:utf-8 -*-
import hashlib
import os
import re

import yaml


def set_config(data: dict, yaml_filename: str):
    """
    将配置写入yaml文件
    :param data:
    :param yaml_filename:
    :return:
    """
    with open(yaml_filename, 'w', encoding="utf-8") as f:
        f.write(yaml.dump(data))


def get_config(yaml_filename: str) -> dict:
    """
    读取yaml配置文件，并返回一个字典
    :param yaml_filename:
    :return:
    """
    with open(yaml_filename, 'r', encoding="utf-8") as f:
        file_data = f.read()
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data


def delete_target_dir(target_dir: str):
    """
    清空一个路径 递归删除其下的所有文件和文件夹
    :param target_dir:
    :return:
    """
    if not os.path.exists(target_dir):
        return
    files = os.listdir(target_dir)
    for file in files:
        file = os.path.join(target_dir, file)
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            delete_target_dir(file)
        else:
            print('参数错误')
    os.removedirs(target_dir)


def get_safe_file_name(file_name: str) -> str:
    """
    过滤文件名中的非法字符
    :param file_name:
    :return:
    """
    return re.sub(r'[<,>,/,\\,|,:,",\',.,*,?]', '-', file_name)


def md5(data: str) -> str:
    """
    生成一个md5值
    :param data:
    :return:
    """
    return hashlib.md5(bytes(data, encoding='utf-8')).hexdigest()


def main():
    pass


if __name__ == '__main__':
    main()
