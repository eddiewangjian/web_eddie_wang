#!/usr/bin/env python
#coding=utf8
import os
import sys
import MySQLdb
import datetime

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../../')

from lib.util.common_error import ErrorCode
from lib.util.common_log import Log
from lib.util.common_mysql import Mysql
from lib.util.common_conf import Conf

class DaoMysqlTmTest:
    def __init__(self):
        self.host = Conf.get_value_str("conf/server.conf", "mysql_tm_test", "host")
        self.port = int(Conf.get_value_str("conf/server.conf", "mysql_tm_test", "port"))
        self.user = Conf.get_value_str("conf/server.conf", "mysql_tm_test", "user")
        self.passwd = Conf.get_value_str("conf/server.conf", "mysql_tm_test", "passwd")
        self.db = Conf.get_value_str("conf/server.conf", "mysql_tm_test", "db")
        Log.info("host={} port={} db={}".format(self.host, self.port, self.db))

    def query_mysql(self, sql):
        return Mysql.query(self.host, self.port, self.db, self.user, self.passwd, sql) 

    def get_node_info(self, taskid):
        """根据任务id获取所有子任务处理信息"""
        sql = "select node_id, node_desc, status, start_time, end_time, proc_addr, real_version from node_info where node_id like '{0}%' and node_type='flow'".format(taskid)
        Log.debug("get_node_info. sql={}".format(sql))
        ret = self.query_mysql(sql)
        if not ret is None:
            return ret
        return None


if __name__ == '__main__':
    dao = DaoMysqlTmTest()
    res = dao.get_node_info("task_daqian_24_13738_paashuaziyuanxuqiumode_20191125_bb_1245465_2019_11_25_17_53_30_492478")
    print res



