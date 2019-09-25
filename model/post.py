#!/usr/bin/python3
#coding=utf8

from model import Model
from hashlib import sha256

class Post(Model):

    def __init__(self, publish_date, length, user, topic, thread, content):
        super().__init__()
        self._publish_date = publish_date
        self._length = length
        self._user = user
        self._topic = topic
        self._thread = thread
        self._hash = sha256(content).hexdigest()

    @property
    def publish_date(self):
        return self._publish_date
    
    @publish_date.setter
    def publish_date(self, publish_date):
        self._publish_date = publish_date

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def user(self):
        return self._user

    # TODO: add typecheck
    @user.setter
    def user(self, user):
        self._user = user

    @property
    def topic(self):
        return self._topic

    # TODO: Add type check
    @topic.setter
    def topic(self, topic):
        self._topic = topic

    @property
    def thread(self):
        return self._thread

    @thread.setter
    def thread(self, thread):
        self._thread = thread

    @property
    def hash(self):
        return self._hash

    def update_hash(self, content):
        self._hash = sha256(content).hexdigest()
