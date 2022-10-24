import sqlite3
import random
from faker import Faker


def create_tbl_person(conn):
    cur = conn.cursor()
    sql = '''
        create table if not exists person(
            person_id integer not null primary key,
            first_name varchar(128) not null,
            last_name varchar(128) not null,
            address varchar(1024) not null,
            job varchar(128) not null,
            age integer
        )
    '''
    cur.execute(sql)


def input_data_person(conn, rec_count):
    cur = conn.cursor()
    p = Faker('uk_UA')
    for _ in range(rec_count):
        sql = f'''
            insert into person (first_name, last_name, address, job, age)
            values
                ("{p.first_name()}", "{p.last_name()}", "{p.address()}", "{p.job()}", {random.randint(20, 60)})
        '''
        cur.execute(sql)
        conn.commit()


def upd_person(conn, person_id, age):
    cur = conn.cursor()
    sql = f'''
        update person
        set age = {age}
        where person_id = {person_id} 
    '''
    cur.execute(sql)
    conn.commit()


def del_all_data(conn):
    cur = conn.cursor()
    sql = f'''delete from person   '''
    cur.execute(sql)
    conn.commit()


def del_person_by_id(conn, person_id):
    cur = conn.cursor()
    sql = f'''
        delete from person where id = {person_id}
    '''
    cur.execute(sql)
    conn.commit()


def output_person(conn):
    cur = conn.cursor()
    sql = '''
            select * from person
        '''
    persons = cur.execute(sql)
    for m in persons:
        print(m)


con = sqlite3.connect('hw_db.db')

create_tbl_person(con)
del_all_data(con)
input_data_person(con, random.randint(11, 31))
# upd_person(con, 6, 77)
output_person(con)
print('Ok')

con.close()
