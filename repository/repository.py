#!/usr/bin/python3
#coding=utf8

class Repository:

    def __init__(self, db, table, fields):
        self.db = db
        self.table = table
        self.fields = fields
    
    def get(id):
        query = ("SELECT " +
                self.fields + " FROM " +
                "self.table WHERE id=%s")
        cursor = self.db.cursor()
        cursor.execure(query, (id))
        entity = cursor.fetchone()
        cursor.close()
        return entity

    def add:
        print("dummy")

    def update():
        print("dummy")

    def delete():
        print("dummy")
    
