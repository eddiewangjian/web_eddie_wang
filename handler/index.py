import os
import sys
import tornado.web

this_file_path = os.path.dirname(os.path.abspath(__file__))

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

