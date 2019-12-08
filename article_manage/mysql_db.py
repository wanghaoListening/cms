import pymysql


class MysqlConn(object):

    __instance = None

    def __init__(self):
        self.conn =pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="cms")
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 关数据库

    def close_db(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    # 查看数据

    def select(self, sql, args=None):
        self.cursor.execute(sql, args)
        rs = self.cursor.fetchall()
        return rs

    def execute(self, sql, args):
        try:
            self.cursor.execute(sql, args)
            affected = self.cursor.rowcount
            # self.conn.commit()
        except BaseException as e:
            print(e)
        return affected

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance