#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import requests.exceptions

ROOT_URL = 'https://www.instagram.com/'
LOGIN_URL = 'https://www.instagram.com/accounts/login/ajax/'
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
ACCEPT_LANGUAGE = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'


class ResponseStatus():
    def __init__(self, success, results, message):
        self.success = success
        self.results = results
        self.message = message


def get_csrftoken():
    headers = {'User-Agent': USER_AGENT}
    with requests.Session() as session:
        resp = session.get(ROOT_URL, headers=headers)
        return resp.cookies['csrftoken']


def do_login(login, password):

    success = False
    results = None
    message = ''

    login_post = {
        'username': login,
        'password': password
    }

    try:

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
                success = data.get("authenticated", False)
                if not success:
                    message = "Ошибка аутентификации"
            else:
                message = resp_login.status_code

    except requests.exceptions.RequestException as e:
        print(e)
        return ResponseStatus(False, None, e)

    return ResponseStatus(success, results, message)


if __name__ == "__main__":
    #csrftoken = get_csrf_token()
    resp = do_login("ptsibizov", "animes123")
    print(resp.success, resp.message)