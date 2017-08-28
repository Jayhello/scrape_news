# _*_ coding:utf-8 _*_

import logging
import json
import os
import logging.config


def setup_logging(default_path = 'logging.json',
                  default_level = logging.INFO,
                  env_key = 'LOG_CFG'):

    path = default_path
    env_key = 'LOG_CFG'
    value = os.getenv(env_key)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def get_logger(path):
    setup_logging(default_path=path)
    return logging.getLogger('loggers')

if __name__=='__main__':
    path = '../config/logging.json'
    # setup_logging(path)
    # logger = logging.getLogger('loggers')
    # logger.info('我的老家'.decode("utf8"))
    print '我的老家'.decode("utf8")
    print type('我的老家'.decode("utf8"))