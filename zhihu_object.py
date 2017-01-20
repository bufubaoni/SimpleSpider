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
        self._first_html = self.get_first_html()
        self._current_page = 1
        self._pages = self.get_pages()
        self._api_content = self.get_api_object()
        self._api_url = api_url

    def get_first_html(self):
        self._html = self._session.get(headers=self._headers, url=self._url).text
        return self._html

    def get_pages(self):
        _get_pages = pq(self._html)("div.Pagination>button")
        if _get_pages:
            return int(_get_pages[-2].text)
        else:
            return 1

    def get_next_page_url(self):
        return self._url + "?page={page}".format(page=self._current_page + 1)

    def get_next_html(self):
        if self._current_page < self._pages:
            self._html = self._session.get(headers=self._headers, url=self.get_next_page_url()).text
            return self._html
        else:
            return None

    def get_html(self):
        return self._html

    def get_api_object(self):
        return self._session.get(headers=self._headers, url=self._api_url).text


if __name__ == "__main__":
    # zhihu = ZhiHuSpider()
    # print zhihu.get_first_html()
    pass
