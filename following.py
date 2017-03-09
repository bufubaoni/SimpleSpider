#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/20
from zhihu_object import ZhiHuSpider


class Following(ZhiHuSpider):
    def __init__(self, url_token):
        # chen-er-bai-18
        self._url = ("https://www.zhihu.com/api/v4/members/{url_token}/followees?"
                     "include=data[*].answer_count,"
                     "articles_count,"
                     "follower_count,"
                     "is_followed,"
                     "is_following,"
                     "badge[?(type=best_answerer)].topics&offset={offset}&limit=20")
        super(Following, self).__init__(self._url, url_token)

if __name__ == "__main__":
    fling = Following(url_token="chen-er-bai-18")

    for i in fling.get_api_object():
        print i["name"], i["url_token"]