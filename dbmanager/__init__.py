#!/usr/bin/python
# -*- coding: utf-8 -*-

import peewee as pw
import models

db = pw.SqliteDatabase('data.db', pragmas=(('foreign_keys', 'on'),))


def initialize():
    db.connect()
    models.Project.create_table(True)
    models.Account.create_table(True)
    models.TaskFollowing.create_table(True)


def create_account(account):
    result = False
    #if not is_exist_account(account.login):
    account.save()
    result = True
    return result


def is_exist_account(login):
    result = models.Account.select().where(models.Account.login == login)
    return True if result.exists() else False


def delete_account(login):
    q = models.Account.delete().where(models.Account.login == login)
    q.execute()


def update_account(account):
    account.save()


def get_all_accounts():
    return list(models.Account.select())


def get_accounts_for_project(project_id):
    return list(models.Account.select().where(models.Account.project == project_id).order_by(models.Account.login))


def create_project(name):
    project = models.Project(name=name)
    project.save()
    return project


def update_project(project):
    project.save()


def delete_project(name):
    #q = models.Project.delete().where(models.Project.name == name)
    #q.execute()
    project = get_project_by_name(name)
    project.delete_instance(recursive=True, delete_nullable=True)


def get_project_by_name(name):
    project = models.Project.get(models.Project.name == name)
    return project


def get_all_projects():
    return list(models.Project.select().order_by(models.Project.name))


def is_exist_project(name):
    result = models.Project.select().where(models.Project.name == name)
    return True if result.exists() else False


def create_task_following(path, delay_from, delay_to, count_to_follow, dont_follow_to_private,
                          dont_follow_to_followers, to_like, count_likes_for_user, to_like_random,
                          use_random_pause, pause_per_users, pause_from, pause_to, login,
                          count_all, count_done):
    task_following = models.TaskFollowing(path=path, delay_from=delay_from, delay_to=delay_to,
                                          count_to_follow=count_to_follow,
                                          dont_follow_to_private=dont_follow_to_private,
                                          dont_follow_to_followers=dont_follow_to_followers,
                                          to_like=to_like, count_likes_for_user=count_likes_for_user,
                                          to_like_random=to_like_random, use_random_pause=use_random_pause,
                                          pause_per_users=pause_per_users, pause_from=pause_from,
                                          pause_to=pause_to, login=login, count_all=count_all,
                                          count_done=count_done)
    task_following.save()


def get_all_tasks_following():
    return list(models.Project.select())


if __name__ == "__main__":
    initialize()
    #print(get_all_accounts())
    if not is_exist_account("user1"):
        create_account("user1", "1234567", '9999', 0, 0)
    #print(get_all_accounts())
    create_project("новый")
    create_task_following("", 1, 2, 500, True, True, True, 5, True, True,
                          20, 2, 4, "user1", 1000, 0)
