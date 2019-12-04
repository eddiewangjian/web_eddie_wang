#coding=utf8
import os
import sys
import MySQLdb

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../../')

from lib.util.common_error import ErrorCode
from lib.util.common_log import Log

class Mysql:
    # 静态单链接请求,如果失败返回None否则返回一个二维list
    @staticmethod
    def query(host, port, db, user, passwd, sql):
        try: 
            conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
            cursor = conn.cursor()
        except Exception as e:
            Log.error("failed to connect mysql. error_msg={}".format(e))
            return None

        res = []
        try:
            count = cursor.execute(sql)
            for item in cursor.fetchall():
                res.append(item)
        except Exception as e:
            Log.error("failed to execute sql. error_msg={}".format(e))
            cursor.close()
            conn.close()
            return None

        cursor.close()
        conn.close()
        return res

if __name__ == '__main__':
    res = Mysql.query("127.0.0.1", 3306, "test", "work", "gsq@123", "select * from user_info")
    print res
    
    res = Mysql.query("127.0.0.1", 3306, "test", "work", "gsq@123", "select count(*) from user_info")
    print res
