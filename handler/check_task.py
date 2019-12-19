import os
import sys
import tornado.web

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../../')

from lib.util.common_error import ErrorCode
from lib.util.common_log import Log
from lib.util.common_mysql import Mysql
from lib.util.common_conf import Conf
from lib.dao.dao_mysql_tm_test import DaoMysqlTmTest
from lib.dao.dao_mysql_tm_online import DaoMysqlTmOnline
from lib.dao.dao_mysql_tm_old import DaoMysqlTmOld

class CheckTaskHandler(tornado.web.RequestHandler):
    def post(self):
        task_id = self.get_argument("task_id")
        Log.info("check_task. task_id={0}".format(task_id))
        if task_id == '':
            self.write("task_id is empty.")
        
        dao = DaoMysqlTmTest()
        info = dao.get_node_info(task_id)
        if info is not None and len(info) > 0:
            self.render("check_task.html", environment='test', check_res=info)
            return

        dao = DaoMysqlTmOnline()
        info = dao.get_node_info(task_id)
        if info is not None and len(info) > 0:
            self.render("check_task.html", environment='online', check_res=info)
            return

        dao = DaoMysqlTmOld()
        info = dao.get_node_info(task_id)
        if info is not None and len(info) > 0:
            self.render("check_task.html", environment='online_old_framework', check_res=info)
            return

        self.render("check_task.html", environment=None, check_res=None)




