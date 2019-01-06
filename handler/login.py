import os
import sys
import tornado.web

this_file_path = os.path.dirname(os.path.abspath(__file__))
from dao.mysql import DaoMysql

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        self.render("login.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        sql = "select * from users where username = '{0}'".format(username)
        user_infos = DaoMysql.query(sql)
        if user_infos:
            db_password = user_infos[0][2]
            if db_password == password:
                self.write("welcome you: " + username)
            else:
                self.write("your password was not right.")
        else:
            self.write("there is no this user.")


