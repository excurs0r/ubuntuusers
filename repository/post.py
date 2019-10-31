#!/usr/bin/python3
#coding=utf8

from model.post import Post

class PostRepository:

    def __init__(self, db):
        self.db = db

    def get(self, id):
        query = ( "SELECT id, publish_date, length, user, topic, thread, hash "
                "FROM post WHERE id=%s")
        cursor = self.db.cursor(query, (id))
        sql_result = cursor.fetchone()
        cursor.close()
        post = Post(sql_result[1], sql_result[2], sql_result[3], sql_result[4])
        post.id = sql_result[0]
        post.hash = sql_result[5]
        return post

    def add(self, post):
        query = ("INSERT INTO post"
                "(publish_date, length, user, topic, thread, hash) "
                "VALUES (%s, %s, %s)")
        cursor = self.db.cursor()
        cursor.execute(query, (post.publish_date, post.length, post.user, post.topic, post.thread, post.hash))
        cursor.close()
        
        
