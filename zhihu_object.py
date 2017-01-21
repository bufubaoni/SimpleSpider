#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/20
from requests import Session
from user_headers import headers
from json import loads


class ZhiHuSpider(object):
    def __init__(self, url):
        self._url = url
        self._headers = headers
        self._session = Session()
        self._current_numbers = 0
        self._totals = 0


    def get_url(self):
        _url = self._url
        return _url.format(offset=self._current_numbers)

    def get_api_object(self):
        objects = loads(self._session.get(headers=self._headers, url=self.get_url()).text)

        if not self._totals:
            self._totals = int(objects["paging"]["totals"])

        self._current_numbers += 20
        print self._current_numbers
        if self._current_numbers < self._totals:
            self.get_api_object()

        yield objects["data"]


if __name__ == "__main__":
    # zhihu = ZhiHuSpider()
    # print zhihu.get_first_html()
    pass
