#!/usr/bin/python
# -*- coding: utf-8 -*-

import peewee as pw

db = pw.SqliteDatabase('data.db')


class Account(pw.Model):
    login = pw.CharField(unique=True)
    password = pw.CharField()
    follows = pw.IntegerField()
    followers = pw.IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.