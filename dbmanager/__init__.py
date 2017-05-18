#!/usr/bin/python
# -*- coding: utf-8 -*-

import peewee as pw
import models

db = pw.SqliteDatabase('data.db')


def initialize():
    db.connect()
    models.Account.create_table(True)


def create_account(login, password, follows, followers):
    result = False
    if not is_exist_account(login):
        acc = models.Account(login=login, password=password, follows=follows, followers=followers)
        acc.save()
        result = True
    return result


def is_exist_account(login):
    result = models.Account.select().where(models.Account.login == login)
    return True if result.exists() else False


def get_all_accounts():
    return list(models.Account.select())


if __name__ == "__main__":
    initialize()
    print(get_all_accounts())
    if not is_exist_account("user1"):
        create_account("user1", "1234567", 0, 0)
    print(get_all_accounts())