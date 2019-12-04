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

class DaoMysqlTmOld:
    def __init__(self):
        self.host = Conf.get_value_str("conf/server.conf", "mysql_tm_old", "host")
        self.port = int(Conf.get_value_str("conf/server.conf", "mysql_tm_old", "port"))
        self.user = Conf.get_value_str("conf/server.conf", "mysql_tm_old", "user")
        self.passwd = Conf.get_value_str("conf/server.conf", "mysql_tm_old", "passwd")
        self.db = Conf.get_value_str("conf/server.conf", "mysql_tm_old", "db")
        Log.info("host={} port={} db={}".format(self.host, self.port, self.db))

    def query_mysql(self, sql):
        return Mysql.query(self.host, self.port, self.db, self.user, self.passwd, sql) 

    def get_node_info(self, taskid):
        """根据任务id获取所有子任务处理信息"""
        sql = "select task_id , 'no support', status, start_ts, end_ts, host, 'no support' from detail_task_info_table where task_id like '{0}%' and sub_task_num = 0".format(taskid)
        Log.debug("get_node_info. sql={}".format(sql))
        ret = self.query_mysql(sql)
        if not ret is None:
            return ret
        return None


if __name__ == '__main__':
    dao = DaoMysqlTmOld()
    res = dao.get_node_info("task_daqian_25_16920_GXQZ_huhuohaotegengxinqianzhi_20191026_1242559")
    print res



