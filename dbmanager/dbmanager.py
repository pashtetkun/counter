#!/usr/bin/python
# -*- coding: utf-8 -*-

import peewee as pw
from models import account

db = pw.SqliteDatabase('data.db')


def create_tables():
    db.create_tables([account.Account], safe=True)


def create_account(login, password):
    acc = account.Account(login=login, password=password)
    acc.save()


if __name__ == "__main__":
    create_tables()
    create_account("user1", "1234567")