import os
import sys
import tornado.web

this_file_path = os.path.dirname(os.path.abspath(__file__))
from dao.mysql import DaoMysql

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("user")
        sql = "select * from users where username = '{0}'".format(username)
        user_infos = DaoMysql.query(sql)
        self.render("index.html", user_infos)

