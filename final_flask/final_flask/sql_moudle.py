import pymysql
from flask import session

class Sql_class():
    def get_conn(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='wz')
        cur = conn.cursor()
        return conn, cur

    def close(self, conn, cur):
        cur.close()
        conn.close()

    def normal_ex(self, conn, cur, sql):
        cur.execute(sql)
        conn.commit()

    def query(self, cur, sql):
        cur.execute(sql)
        results = cur.fetchall()
        return results

def get_current_usr_zan_wz_list():
    get_now_usr_zan_list_sql = '''
    select t1.title  ,t1.usr_name as author, t2.usr_id as zaner, t1.content, t1.id as wz_id
    from
    (SELECT u.alias_name, w.title,w.content , u.usr_name, w.id
        FROM wz.usr u, wz.wz_all w 
        where u.usr_name=w.usr_name and w.usr_name='{current_usr}') t1
    left join
    (select z.wz_id,z.usr_id,u.alias_name
        from wz.zan z,  wz.usr u
        where z.usr_id=u.usr_name) t2
    on t1.id=t2.wz_id and t2.usr_id='{current_usr}';
    '''.format(current_usr=session.get('username'))
    conn, cur = cls.get_conn()
    now_usr_zan_list = cls.query(cur, get_now_usr_zan_list_sql)
    cls.close(conn, cur)
    return now_usr_zan_list


def get_all_display_wz_data():
    get_all_display_wz_data_sql = '''
    SELECT t3.title, t3.author, t3.content, Count(t3.zaner) as count_zan, t3.id
    FROM   
    (SELECT t1.usr_name as author, t1.content, t1.title, t1.id, t2.usr_id   as zaner
        FROM 
            (SELECT u.alias_name, w.title, w.content, u.usr_name, w.id
                FROM   wz.usr u, wz.wz_all w
                WHERE  u.usr_name = w.usr_name) t1
            LEFT OUTER JOIN 
            (SELECT z.wz_id, z.usr_id, u.alias_name
                FROM   wz.zan z, wz.usr u
                WHERE  z.usr_id = u.usr_name) t2
    ON t1.id = t2.wz_id) t3
    GROUP  BY t3.title,
              t3.author; 
    '''
    conn, cur = cls.get_conn()
    now_display_wz_data = cls.query(cur, get_all_display_wz_data_sql)
    print(now_display_wz_data)
    cls.close(conn, cur)
    return now_display_wz_data


def get_wz_html_data(id):
    wz_sql = '''
    SELECT w.usr_name as author, w.title, w.content
    FROM   wz.wz_all as w
    WHERE  id={current_id};
    '''.format(current_id=id)
    zan_sql = '''
    select z.usr_id as zaner
    from wz.zan as z
    where z.wz_id = {current_id};
    '''.format(current_id=id)
    conn, cur = cls.get_conn()
    wz_data = cls.query(cur, wz_sql)
    zan_data = cls.query(cur, zan_sql)
    print(wz_data)
    print(zan_data)
    cls.close(conn, cur)
    return wz_data, zan_data

