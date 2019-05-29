# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:48:33 2019

@author: DWrenne
"""

from copy import copy
import json
import logging
import requests
import urllib

try:
    import cookielib
except ImportError:
    import http.cookiejar as cookielib


class Poster(object):

    def log(self, s):
        if True:
            print(s)
            
    def __init__(self, endpoint=None, cookieFile='cookies.txt'):
        self.session = requests.Session()
        self.session.headers = {'content-type': 'application/json', 'accept': 'application/json'}
        cj = cookielib.FileCookieJar(cookieFile)
        self.session.cookies = cj
        if endpoint is None:
            self.endpoint = self._get_endpoint()
        else:
            self.endpoint = endpoint

    def _get_endpoint(self):

        endpoint = self.endpoint  
        return endpoint

    def post(self, payload, headers=None):
        self.session.headers['Content-Type'] = "application/json"
        print(self.session.headers)
        r = self.session.post(self.endpoint, data=json.dumps(payload), headers=headers)
        r.raise_for_status()
        return r