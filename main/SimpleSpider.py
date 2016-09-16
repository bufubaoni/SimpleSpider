#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SpiderGetConf import SpiderGetConf
import requests
from pyquery import PyQuery as pq


class SimpleSpider(object):
    def __init__(self, path, **kwargs):
        self._config = SpiderGetConf(path).getConfig()
        self._headers = self._config["headers"]
        self._base = self._config["base"]
        self._requests = "requests"
        self._ulrlist = "urllist"
        self._nextpage = "nextpage"
        self._method = "method"
        self._requestsagrs=list()
        self._requestkwagrs=dict()

    def setRequest(self, request):
        if callable(request):
            def newfun(*a, **kwargs):
                print(kwargs)
                self._requestsagrs.extend(*a)
                self._requestkwagrs.update(**kwargs)

                request(*a, **kwargs)
            self._requests = newfun
        else:
            pass

    def setAnalytical(self, method):
        if callable(method):
            self._method = method
        else:
            pass

    def getHeaders(self):
        return self._headers

    def getContent(self):
        pass


if __name__ == "__main__":
    spider = SimpleSpider("conf/firs.conf")
    spider.setRequest(requests.get)
    content = spider.getContent()
    print(spider.getHeaders())
    print(content)
