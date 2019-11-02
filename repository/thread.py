#!/usr/bin/python3
#coding=utf8

from model.thread import Thread

class ThreadRepository:

    def __init__(self, db):
        self.db = db

    def get(self, id):
        query = ("SELECT id, name, url, topic FROM thread"
                "WHERE id=%s")
        cursor = self.db.cursor()
        cursor.execute(query, (id))
        sql_result = cursor.fetchone()
        cursor.close()
        thread = Thread(sql_result[1], sql_result[2], sql_result[3])
        thread.id = sql_result[0]
        return thread 

    def add(self,thread):
        query = ("INSERT INTO thread (name, url, topic) "
                "VALUES (%s, %s, %s)")
        cursor = self.db.cursor()
        cursor.execute(query, (thread.name, thread.url, thread.topic))
        cursor.close()
        self.db.commit()
       
    def get_paginated(self, page=1, items=20):
        query = ("SELECT id, name, url, topic FROM "
                 "thread LIMIT %s OFFSET %s;")
        cursor = self.db.cursor()
        cursor.execute(query, (items, items*(page-1)))
        threads = cursor.fetchall()
        cursor.close()
        if len(threads) == 0:
            return False
        thread_models = []
        for t in threads:
            thread = Thread(t[1], t[2], t[3])
            thread.id = t[0]
            thread_models.append(thread)
        return thread_models
