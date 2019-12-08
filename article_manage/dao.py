import mysql_db
import datetime as date


class CategoryDao(object):

    def save(self, category):
        sql = "insert into cms_category (id,c_name,c_desc,gmt_create,gmt_Modify) VALUES (%s, %s, %s, %s, %s)"
        mysql_conn = mysql_db.MysqlConn()
        try:
            # 生成当前时间
            curr_datetime = date.datetime.now()
            result = mysql_conn.execute(sql, (None, category.get_name(), category.get_desc(), curr_datetime, curr_datetime))
            return 1 == result
        finally:
            mysql_conn.commit()
            return False

    def get_by_id(self, c_id):
        sql = "select id,c_name,c_desc from cms_category where id = %s"
        mysql_conn = mysql_db.MysqlConn()
        return mysql_conn.select(sql, (c_id,))

    def delete_by_id(self, c_id):
        sql = "delete from cms_category where id = %s"
        mysql_conn = mysql_db.MysqlConn()
        try:
            return mysql_conn.execute(sql, (c_id,))
        finally:
            mysql_conn.commit()
            return 1

    def list(self):
        sql_prefix = "select * from cms_category"
        mysql_conn = mysql_db.MysqlConn()
        return mysql_conn.select(sql_prefix, ())


class ItemDao(object):

    def save(self, item):
        sql = "insert into cms_item (i_title,i_content,c_id,gmt_create,gmt_Modify) VALUES (%s, %s, %s, %s, %s)"
        mysql_conn = mysql_db.MysqlConn()
        try:
            # 生成当前时间
            curr_datetime = date.datetime.now()
            result = mysql_conn.execute(sql, (item.get_title(), item.get_content(), item.get_cid(), curr_datetime, curr_datetime))
            return result == 1
        finally:
            mysql_conn.commit()
            return False

    def get_by_id(self, i_id):
        sql = "select id,i_content,c_id,gmt_create,i_title from cms_item where id = %s"
        mysql_conn = mysql_db.MysqlConn()
        return mysql_conn.select(sql, (i_id,))[0]

    def delete_by_id(self, i_id):
        sql = "delete from cms_item where id = %s"
        mysql_conn = mysql_db.MysqlConn()
        try:
            return mysql_conn.execute(sql, (i_id,))
        finally:
            mysql_conn.commit()
            return 1

    def list_by_cid(self, c_id):
        sql = "select id,i_content,c_id,i_title,gmt_create from cms_item where c_id = %s"
        mysql_conn = mysql_db.MysqlConn()
        return mysql_conn.select(sql, (c_id,))

    def list(self, params):
        sql = "list"
        mysql_conn = mysql_db.MysqlConn()
        mysql_conn.select(sql, params)
        return None
