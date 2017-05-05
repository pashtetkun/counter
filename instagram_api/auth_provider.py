#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

ROOT_URL = 'https://www.instagram.com/'
LOGIN_URL = 'https://www.instagram.com/accounts/login/ajax/'
USER_AGENT = 'Mozilla/5.0'


def get_csrf_token():
    headers = {'User-Agent': USER_AGENT}
    with requests.Session() as session:
        resp = session.get(ROOT_URL, headers=headers)
        return resp.cookies['csrftoken']


def doLogin(username, password, csrftoken):
    headers = {}
    headers['User-Agent'] = USER_AGENT
    headers["X-CSRFToken"] = csrftoken
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["X-Instagram-AJAX"] = "1"
    headers["Referer"] = 'https://www.instagram.com/'
    payload = {'username':username, 'password':password}

    resp = requests.post(LOGIN_URL, headers=headers, data=payload)
    print(resp.text)


if __name__ == "__main__":
    csrftoken = get_csrf_token()
    doLogin("ptsibizov", "animes12", csrftoken)

