#!/usr/bin/python3
#coding=utf8

class UserRepository:

    def __init__(self, db):
        self.db = db

    def get(self, id):
        query = (" SELECT id, username, register_date"
        "FROM user WHERE id={id};")
        cursor = self.db.cursor()
        data = cursor.execute(query.format(id=id))
        curs0r.close()
        return data.fetchone()



    def add(self, username, register_date):
        query = (" INSERT INTO user "
        "(username, register_date) "
        "VALUES (%s, %s);")
        cursor = self.db.cursor()
        cursor.execute(query, (username, register_date))
        cursor.execute('select username, register_date from user limit 2')
        for user in cursor.fetchall():
            print("User {username} registered {date}".format(username=user[0],date=user[1]))
        cursor.close()
