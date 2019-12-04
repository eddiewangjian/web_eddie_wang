#coding=utf-8
import os
import sys
import logging
import traceback

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../../')

from lib.util.common_conf import Conf

class Log:
    @staticmethod
    def init():
        try:
            logger = logging.getLogger(__name__)
            if logger is None:
                print "failed to getlogger."
                return 1

            path = Conf.get_value_str("conf/server.conf", "log", "path")
            if path is None:
                print "failed to get_value_str. conf_path=conf/server.conf section=log key=path"
                return 1;
            if len(path) > 0 and path[0] != '/':
                path = Conf.get_root_path() + path
            handler = logging.FileHandler(path)

            level = int(Conf.get_value_str("conf/server.conf", "log", "level"))
            if level is None:
                print "failed to get_value_str. conf_path=conf/server.conf section=log key=level"
                return 1
            logger.setLevel(level)

            formatter = logging.Formatter("[%(levelname)s][%(asctime)s]%(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        except:
            traceback.print_exc()
            print sys.exc_info()[0], sys.exc_info()[1]
            print "failed to init."
            return 1

        return 0

    @staticmethod
    def logger():
        return logging.getLogger(__name__)

    @staticmethod
    def debug(msg):
        logging.getLogger(__name__).debug(msg)

    @staticmethod
    def info(msg):
        logging.getLogger(__name__).info(msg)

    @staticmethod
    def warning(msg):
        logging.getLogger(__name__).warning(msg)

    @staticmethod
    def error(msg):
        logging.getLogger(__name__).error(msg)

    @staticmethod
    def critical(msg):
        logging.getLogger(__name__).critical(msg)

# 全局初始化为了其他模块在不init情况下可直接引用
Log.init()

if __name__ == '__main__':
    Log.init()
    
    Log.logger().info("info")
    Log.logger().error("error")

    Log.debug("debug")
    Log.info("info")
    Log.warning("warning")
    Log.error("error")
    Log.critical("critical")









