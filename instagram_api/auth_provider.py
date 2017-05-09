#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

ROOT_URL = 'https://www.instagram.com/'
LOGIN_URL = 'https://www.instagram.com/accounts/login/ajax/'
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
ACCEPT_LANGUAGE = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'


def get_csrf_token():
    headers = {'User-Agent': USER_AGENT}
    with requests.Session() as session:
        resp = session.get(ROOT_URL, headers=headers)
        return resp.cookies['csrftoken']


def doLogin(login, password):

    result = False
    """headers = {}
    headers['User-Agent'] = USER_AGENT
    headers["X-CSRFToken"] = csrftoken
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["X-Instagram-AJAX"] = "1"
    headers["Referer"] = 'https://www.instagram.com/'
    payload = {'username':username, 'password':password}"""

    login_post = {
        'username': login,
        'password': password
    }

    with requests.Session() as session:
        session.cookies.update({
            'sessionid': '',
            'mid': '',
            'ig_pr': '1',
            'ig_vw': '1920',
            'csrftoken': '',
            's_network': '',
            'ds_user_id': ''
        })
        session.headers.update({
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': '*',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'www.instagram.com',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'User-Agent': USER_AGENT,
            'X-Instagram-AJAX': '1',
            'X-Requested-With': 'XMLHttpRequest'
        })

        resp = session.get(ROOT_URL)
        session.headers.update({'X-CSRFToken': resp.cookies['csrftoken']})
        resp_login = session.post(LOGIN_URL, data=login_post,  allow_redirects=True)
        csrftoken = resp_login.cookies['csrftoken']
        session.headers.update({'X-CSRFToken': csrftoken})
        if resp_login.status_code == 200:
            data = resp_login.json()
            result = data.get("authenticated", False)
        else:
            print('login error!')

    return result


if __name__ == "__main__":
    #csrftoken = get_csrf_token()
    doLogin("ptsibizov", "animes12")

