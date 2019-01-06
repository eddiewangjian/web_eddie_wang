# coding=utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import tornado.web

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../')
from url import url

print "debug:", this_file_path, os.path.join(this_file_path, "/../template")
settings = dict(
    template_path = this_file_path + "/../template",
	static_path = this_file_path + "/../static"
)

application = tornado.web.Application(handlers=url, debug=True, **settings)
