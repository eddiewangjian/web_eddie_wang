import MySQLdb

class DaoMysql:
    def __init__(self):
        pass

    @staticmethod
    def query(sql):
        conn = MySQLdb.connect(host="localhost", port=3306, user="work",passwd="gsq@123",db="web_eddie_wang",charset="utf8")
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        lines = cur.fetchall()
        return lines




