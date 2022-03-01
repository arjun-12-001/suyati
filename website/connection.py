import psycopg2 as pg


def db_val(val):
        if val == 1:
                con = pg.connect(
                host="127.0.0.1",
                database="postgres",
                user="postgres",
                password="arjun@1968")
                cur = con.cursor()
                counter = 0
                cur.execute('select * from public.account where "Class" = 1;')
                row = cur.fetchall()

                cur.close()
                con.close()
        elif val == 0:
                cur = con.cursor()
                counter = 0
                cur.execute('select * from public.account where "Class" = 0;')
                row = cur.fetchall()

                cur.close()
                con.close()
        elif val == 2:
                con = pg.connect(
                host="127.0.0.1",
                database="postgres",
                user="postgres",
                password="arjun@1968")
                cur = con.cursor()
                counter = 0
                cur.execute('select * from account;')
                row = cur.fetchall()

                cur.close()
                con.close()
        return row