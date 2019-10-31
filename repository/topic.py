#!/usr/bin/python3
#coding=utf8

from model.topic import Topic

class TopicRepository:

    def __init__(self, db):
        self.db = db

    def get(self, id):
        query = ("SELECT id, name, url FROM topic"
                "WHERE id=%s")
        cursor = self.db.cursor()
        cursor.execute(query, (id))
        sql_result = cursor.fetchone()
        cursor.close()
        topic = Topic(sql_result[1], sql_result[2])
        topic.id = sql_result[0]
        return topic

    def add(self, topic):
        query = ("INSERT INTO topic (name, url)"
                "VALUES (%s, %s)")
        cursor = self.db.cursor()
        cursor.execute(query, (topic.name, topic.url))
        cursor.close()
        self.db.commit()
        

    def get_topics(self, page=1, items=20):
        query = ("SELECT id, name, url FROM "
                "topic LIMIT %s OFFSET %s;")
        cursor = self.db.cursor()
        cursor.execute(query, (items, items*(page-1)))
        topics = cursor.fetchall()
        cursor.close()
        if len(topics) == 0:
            return False
        topic_models = []
        for t in topics:
            model = Topic(t[1], t[2])
            model.id = t[0]
            topic_models.append(model)
        return topic_models

    def get_by_url(self, url):
        # TODO: Find another way - maybe escape seperately
        query = ("SELECT id, name, url FROM topic  WHERE url='"
                + url + "' LIMIT 1")
        cursor = self.db.cursor()
        cursor.execute(query, (url))
        sql_result = cursor.fetchone()
        cursor.close
        topic = Topic(sql_result[1], sql_result[2])
        topic.id = sql_result[0]
        return topic

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
        
