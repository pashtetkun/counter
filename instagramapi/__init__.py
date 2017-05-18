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


class ResponseStatus():
    def __init__(self, success, results, message):
        self.success = success
        self.results = results
        self.message = message


class InstaWorker:

    ROOT_URL = 'https://www.instagram.com/'
    LOGIN_URL = 'https://www.instagram.com/accounts/login/ajax/'
    USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
    ACCEPT_LANGUAGE = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
    USER_INFO_URL = 'https://www.instagram.com/%s/?__a=1'

    def __init__(self, login, password):
        self.login = login
        self.password = password

        self.session = requests.Session()

    def do_login(self):
        success = False
        results = None
        message = ''

        login_post = {
            'username': self.login,
            'password': self.password
        }

        try:

            with self.session as session:
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
                resp_login = session.post(LOGIN_URL, data=login_post, allow_redirects=True)
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

    def get_account_info(self):
        url = USER_INFO_URL % self.login
        try:
            resp = self.session.get(url)
            user_info = json.loads(resp.text)
            follows = user_info['user']['follows']['count']
            #print("follows:" + str(follows))
            followers = user_info['user']['followed_by']['count']
            return ResponseStatus(True, {"follows": follows, "followers": followers}, "")
        except requests.exceptions.RequestException as e:
            print(e)
            return ResponseStatus(False, None, e)


if __name__ == "__main__":
    #csrftoken = get_csrf_token()
    instaWorker = InstaWorker("ptsibizov", "animes12")
    answer = instaWorker.do_login()
    print(answer.success, answer.message)
    answer1 = instaWorker.get_account_info()
    print(answer.success, answer1.results, answer.message)