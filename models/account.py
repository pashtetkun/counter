#!/usr/bin/python
# -*- coding: utf-8 -*-

from peewee import *

db = SqliteDatabase('data.db')


class Account(Model):
    login = CharField()
    password = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.