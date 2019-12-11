# coding=utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../')

from handler.login import LoginHandler
from handler.index import IndexHandler
from handler.check_task import CheckTaskHandler

url = [
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
    (r'/check_task', CheckTaskHandler),
    (r'/login', LoginHandler),
]
