# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 日志.py
@time: 2020/10/27 13:51
@desc:
"""
import logging


def write_log(info: str, log_file: str = './log.txt'):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S %p"
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    logging.info(info)


def main():
    # LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    # DATE_FORMAT = "%Y-%m-%d %H:%M:%S %p"
    #
    # logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    #
    # logging.debug("This is a debug log.")
    # logging.info("This is a info log.")
    # logging.warning("This is a warning log.")
    # logging.error("This is a error log.")
    # logging.critical("This is a critical log.")
    write_log('这里输出了结果')


if __name__ == '__main__':
    main()
