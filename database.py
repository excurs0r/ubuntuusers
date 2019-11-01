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

db = Database(database['host'], database['user'], database['password'], database['database'])
