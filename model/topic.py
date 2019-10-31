#!/usr/bin/env python3
# coding=utf8

from .model import Model


class Topic(Model):

    def __init__(self, name, url):
        super().__init__()
        self._id = 0;
        self._name = name
        self._url = url

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
