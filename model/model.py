#!/usr/bin/env python3
# coding=utf8


class Model:

    def __init__(self):
        self._id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, _id):
        self._id = _id
