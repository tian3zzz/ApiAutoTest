import logging
from logging import handlers
from config import *
import time


def init_log():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    log_file_name = LOG_PATH + 'log.log' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    fh = handlers.TimedRotatingFileHandler(log_file_name, when='midnight', interval=1,
                                           backupCount=1, encoding='utf-8')
    sh = logging.StreamHandler()
    fh.setLevel(logging.INFO)
    sh.setLevel(logging.INFO)
    # 设置日志格式、创建格式化器
    fmt = '%(asctime)s - %(levelname)s - [%(name)s] - [%(filename)s - (%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器设置到日志器中
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    # 将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh)


init_log()
