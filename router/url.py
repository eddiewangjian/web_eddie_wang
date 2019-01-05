# coding=utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../')

from handler.index import IndexHandler

url = [
    (r'/', IndexHandler),
]
