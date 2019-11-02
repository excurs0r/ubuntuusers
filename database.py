#!/usr/bin/env python3
# coding=utf8

import mysql.connector
from config import database

class Database:

    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(host=host, user=user, password=password, database=database)

    def cursor(self):
        return self.connection.cursor()

    def close(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def truncate(self):
        cursor = self.cursor()
        cursor.execute('SET FOREIGN_KEY_CHECKS=0')
        cursor.execute('truncate table topic')
        cursor.execute('truncate table thread')
        cursor.execute('truncate table post')
        cursor.execute('truncate table user')
        cursor.execute('SET FOREIGN_KEY_CHECKS=1')
        self.commit()

db = Database(database['host'], database['user'], database['password'], database['database'])
