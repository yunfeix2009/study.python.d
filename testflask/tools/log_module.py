import logging
import os
import datetime
# import setting
from os.path import dirname, join


def logFile(fileName, output='all'):
    # 取得当前时间
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
    # 项目根目录
    BASE_PATH = dirname(__file__).replace(r'\/'.replace(os.sep, ''), os.sep)
    # print(BASE_PATH)
    # print(dirname(__file__))
    # 日志保存目录
    LOG_PATH = join(BASE_PATH, "logs")
    path_file = LOG_PATH + r'\{}_{}.log'.format(fileName, now_time).replace(r'\/'.replace(os.sep, ''), os.sep)
    # 设置日志器
    log = logging.getLogger()
    log.setLevel(level=logging.INFO)
    # 设置格式器
    streanFormatter = logging.Formatter(fmt='[%(asctime)s]：[%(levelname)s] '
                                            '->>%(message)s')
    fileFormatter = logging.Formatter(fmt='[%(asctime)s]: [%(filename)s] '
                                          '[%(levelname)s] ''line:%(lineno)d->>%(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
    # 设置控制台处理器
    s_hand = logging.StreamHandler()
    s_hand.setLevel(logging.ERROR)  # 设置处理器级别
    s_hand.setFormatter(streanFormatter)  # 添加控制台格式器
    # 设置文件处理器
    f_hand = logging.FileHandler(filename=path_file, encoding='utf-8')
    f_hand.setLevel(logging.INFO)  # 设置处理器级别
    f_hand.setFormatter(fileFormatter)  # 添加文件格式器

    if output == "all":
        # 日志器添加控制台处理器
        log.addHandler(s_hand)
        # 日志器添加文件处理器
        log.addHandler(f_hand)
        return log
    elif output == 'stream':
        log.addHandler(s_hand)
        return log
    elif output == 'file':
        log.addHandler(f_hand)
        return log
    else:
        raise ValueError("output参数错误")


# logger = logFile(gl.get_val("name"), output='file')
logger = logFile('app', output='stream')
