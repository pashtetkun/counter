#!/usr/bin/python
# -*- coding: utf-8 -*-

import peewee as pw

db = pw.SqliteDatabase('data.db')


class Account(pw.Model):
    project_id = pw.IntegerField(null=True)
    login = pw.CharField(unique=True)
    password = pw.CharField()
    user_id = pw.CharField()
    follows = pw.IntegerField()
    followers = pw.IntegerField()
    use_proxy = pw.BooleanField(default=False)
    proxy_ip = pw.CharField(null=True)
    proxy_port = pw.IntegerField(null=True)
    proxy_protocol = pw.CharField(null=True)
    proxy_login = pw.CharField(null=True)
    proxy_password = pw.CharField(null=True)

    class Meta:
        database = db # This model uses the "people.db" database.


class TaskFollowing(pw.Model):
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

    class Meta:
        database = db # This model uses the "people.db" database.


class Project(pw.Model):
    name = pw.CharField(unique=True)

    class Meta:
        database = db # This model uses the "people.db" database.