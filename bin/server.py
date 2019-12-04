import os
import sys
import tornado.ioloop
from tornado.options import define, options
import tornado.httpserver

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../')
from router.application import application

define("port", default=8000, help="listen port", type=int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print "Development server is running at http://127.0.0.1:%s" % options.port
    print "Quit the server with Control-C"

    tornado.ioloop.IOLoop.instance().start()    
    return 

if __name__ == "__main__":
    main()
