#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import requests.exceptions
import json

ROOT_URL = 'https://www.instagram.com/'
LOGIN_URL = 'https://www.instagram.com/accounts/login/ajax/'
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
ACCEPT_LANGUAGE = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
USER_INFO_URL = 'https://www.instagram.com/%s/?__a=1'
FOLLOW_URL = 'https://www.instagram.com/web/friendships/%s/follow/'

#get user_info without session - success
def get_account_info(user_name):
    url = USER_INFO_URL % user_name
    try:
        resp = requests.get(url)
        user_info = json.loads(resp.text)
        print(user_info)
        follows = user_info['user']['follows']['count']
        # print("follows:" + str(follows))
        followers = user_info['user']['followed_by']['count']
        user_id = user_info['user']['id']
        print(user_id)
        return user_id
    except requests.exceptions.RequestException as e:
        print(e)
        return None


#try follow without session - failure
def do_follow(user_id):
    url = FOLLOW_URL % user_id
    print(url)
    try:
        resp = requests.post(url)
        if resp.status_code == 200:
            print(resp.text)
    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == "__main__":
    user_id = get_account_info("abouttng")
    do_follow(user_id)