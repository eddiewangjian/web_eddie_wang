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

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        self.render("index.html")





