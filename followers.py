#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/20
from zhihu_object import ZhiHuSpider


class Followers(ZhiHuSpider):
    def __init__(self,url_token):
        # chen-er-bai-18
        self._url = ("https://www.zhihu.com/api/v4/members/{name}/followers?"
                     "include=data[*].answer_count,"
                     "articles_count,"
                     "follower_count,"
                     "is_followed,"
                     "is_following,"
                     "badge[?(type=best_answerer)].topics&offset={offset}&limit=20")
        super(Followers, self).__init__(self._url, url_token)

if __name__ == "__main__":
    flers = Followers(url_token="chen-er-bai-18")

    for i in flers.get_api_object():
        print i["name"],i["url_token"]
