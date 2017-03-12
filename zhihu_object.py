#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/20
from requests import Session
from user_headers import headers
from json import loads
import gevent
from gevent import monkey
monkey.patch_all()


class ZhiHuSpider(object):
    def __init__(self, url, url_token):
        self._url = url
        self._url_token = url_token
        self._headers = headers
        self._session = Session()
        self._current_numbers = 0
        self._totals = 0
    
    try:
        pass
    except expression as identifier:
        pass

    def get_url(self, current_number):
        _url = self._url
        _current_numb = self._current_numbers
        print _current_numb
        return _url.format(offset=current_number, url_token=self._url_token)

    def get_api_object(self):

        objects = self._requests(self._current_numbers)

        if not self._totals:
            self._totals = int(objects["paging"]["totals"])

        for item in objects["data"]:
            yield item

        jobs = list()

        while self._current_numbers < self._totals:
            self._current_numbers += 20
            jobs.append(gevent.spawn(self._requests, self._current_numbers))

        gevent.joinall(jobs)

        for job in jobs:
            for item in job.value["data"]:
                yield item

    def _requests(self, url_number):
        
        response = self._session.get(headers=self._headers,
                                     url=self.get_url(url_number))
        
        if response.ok:
            return loads(response.text)
        else:
            response.raise_for_status()


if __name__ == "__main__":
    # zhihu = ZhiHuSpider()
    # print zhihu.get_first_html()
    pass
