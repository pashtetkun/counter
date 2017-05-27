#!/usr/bin/python
# -*- coding: utf-8 -*-

import peewee as pw

db = pw.SqliteDatabase('data.db')


class BaseModel(pw.Model):
    class Meta:
        database = db # This model uses the "people.db" database.


class Project(BaseModel):
    name = pw.CharField(unique=True)


class Account(BaseModel):
    project = pw.ForeignKeyField(Project, related_name='accounts', null=True, on_delete='CASCADE')
    login = pw.CharField(unique=True)
    password = pw.CharField()
    user_id = pw.CharField(null=True)
    follows = pw.IntegerField(null=True)
    followers = pw.IntegerField(null=True)
    use_proxy = pw.BooleanField(default=False)
    proxy_ip = pw.CharField(null=True)
    proxy_port = pw.IntegerField(null=True)
    proxy_protocol = pw.CharField(null=True)
    proxy_login = pw.CharField(null=True)
    proxy_password = pw.CharField(null=True)


class TaskFollowing(BaseModel):
    path = pw.CharField()
    delay_from = pw.IntegerField()
    delay_to = pw.IntegerField()
    count_to_follow = pw.IntegerField()
    dont_follow_to_private = pw.BooleanField()
    dont_follow_to_followers = pw.BooleanField()
    to_like = pw.BooleanField()
    count_likes_for_user = pw.IntegerField()
    to_like_random = pw.BooleanField()
    use_random_pause = pw.BooleanField()
    pause_per_users = pw.IntegerField()
    pause_from = pw.IntegerField()
    pause_to = pw.IntegerField()
    login = pw.CharField(unique=True)
    count_all = pw.IntegerField()
    count_done = pw.IntegerField()