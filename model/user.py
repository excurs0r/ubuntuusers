#!/usr/bin/python3
#coding=utf8

from model import Model

class User(Model):
    
    def __init__(self, username, register_date):
        super().__init__()
        self._username = username
        self._register_date = register_date

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, register_date):
        self._register_date = register_date
