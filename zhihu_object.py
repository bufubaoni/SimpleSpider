#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/20
from requests import Session
from user_headers import headers
from pyquery import PyQuery as pq
import pdb


class ZhiHuSpider(object):
    def __init__(self, url, api_url):
        self._url = url
        self._headers = headers
        self._session = Session()

        self._api_url = api_url
        self._api_content = self.get_api_object()


    def get_api_object(self):
        return self._session.get(headers=self._headers, url=self._api_url).text


if __name__ == "__main__":
    # zhihu = ZhiHuSpider()
    # print zhihu.get_first_html()
    pass
