#!/usr/bin/python3
#coding=utf8

class TopicRepository:

    def __init__(self, db):
        self.db = db

    def get(self, id):
        query = ("SELECT id, name, url FROM topic"
                "WHERE id=%s")
        cursor = self.db.cursor()
        cursor.execute(query, (id))
        topic = cursor.fetchone()
        cursor.close()
        return topic

    def add(self, name, url):
        query = ("INSERT INTO topic (name, url)"
                "VALUES (%s, %s)")
        cursor = self.db.cursor()
        print("Adding: {name}".format(name=name))
        cursor.execute(query, (name, url))
        cursor.close()
        

    # WIP
    def get_topics(self, page=1, items=20):
        query = ("SELECT id, name, url FROM"
                "topic LIMIT %s OFFSET %s;")
        cursor = self.db.cursor()
        cursor.execute(query, (items, items*(page-1)))
        topics = cursor.fetchall()
        cursor.close()
        return topics




    # Buggy
    def exist(self, url):
        query = ("SELECT id FROM topic"
                "WHERE url='%s'")
        cursor = self.db.cursor()
        cursor.execute(query, (url))
        r = cursor.fetchmany()
        cursor.close()
        if len(r) > 0:
            return True
        return False
        
