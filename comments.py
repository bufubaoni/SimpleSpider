#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zhihu_object import ZhiHuSpider


class Comments(ZhiHuSpider):
    def __init__(self, url_token):
        self._url = ("https://www.zhihu.com/api/v4/answers/{url_token}/comments?"
                     "include=data[*].author,"
                     "collapsed,"
                     "reply_to_author,"
                     "disliked,"
                     "content,"
                     "voting,"
                     "vote_count,"
                     "is_parent_author,"
                     "is_author&"
                     "order=normal&"
                     "limit=20&"
                     "status=open"
                     "&offset={offset}")
        super(Comments, self).__init__(self._url, url_token)


if __name__ == "__main__":
    qus = Comments(148848088)
    for k, item in enumerate(qus.get_api_object()):
        print k, item['author']['member']['name'].encode("utf8")
