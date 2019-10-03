#!/usr/bin/env python3
# coding=utf8

from .model import Model


class Post(Model):

    def __init__(self, user, topic, thread):
        super().__init__()
        self._user = user
        self._topic = topic
        self._thread = thread

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, topic):
        self._topic = topic

    @property
    def thread(self):
        return self._thread

    @thread.setter
    def thread(self, thread):
        self._thread = thread
