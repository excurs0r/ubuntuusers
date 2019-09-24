#!/usr/bin/python3
#coding=utf8

import config
import mysql.connector
from mysql.connector import RefreshOption

class Database:

    def __init__(self, host, user, password, database):
       self.connection = mysql.connector.connect(host=host, user=user, password=password, database=database)

    

    def cursor(self):
        return self.connection.cursor()

    def refresh(self):
        self.connection.cmd_refresh(RefreshOption.TABLES)
