#coding=utf-8
import os
import sys
import traceback
import ConfigParser

this_file_path = os.path.dirname(os.path.abspath(__file__))
root_path = this_file_path + '/../../'

class Conf:
    def __init__(self):
        pass

    @staticmethod
    def get_root_path():
        return root_path

    #conf_file:相对部署根路径或绝对路径
    @staticmethod
    def get_value_str(conf_path, section, key):
        if len(conf_path) > 0 and conf_path[0] != '/':
            conf_path = root_path + conf_path
        
        confMgr = ConfigParser.ConfigParser()
        confMgr.read(conf_path)
        try:
            value = confMgr.get(section, key)
            return value
        except:
            traceback.print_exc()
            print sys.exc_info()[0], sys.exc_info()[1]
            return None

#测试函数
if __name__ == "__main__":
    pass
    
    print root_path

    v = Conf.get_value_str("conf/km_client.conf", "server", "port")
    print v
    
    p = Conf.get_root_path()
    print p

