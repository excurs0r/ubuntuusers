#!/usr/bin/python3
#coding=utf8

class PostRepository:

    def __init(selfi, db):
        self.db = db

    def get(self, id):
        query = ( "SELECT id, publish_date, length, user FROM post"
                "WHERE id=%s")
        cursor = self.db.cursor(query, (id))
        post = cursor.fetchone()
        cursor.close()
        return post

    def add(self, publish_date, length, user):
        query = ("INSERT INTO post"
                "(publish_date, length, user)"
                "VALUES (%s, %s, %s)")

        
