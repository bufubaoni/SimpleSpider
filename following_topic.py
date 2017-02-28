#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zhihu_object import ZhiHuSpider


class FollowingTopic(ZhiHuSpider):
    def __init__(self,url_token):
        self._url = ("https://www.zhihu.com/api/v4/members/{url_token}/"
                     "following-topic-contributions?"
                     "include=data[*].topic.introduction"
                     "&offset={offset}"
                     "&limit=20")

        super(FollowingTopic, self).__init__(self._url, url_token)


if __name__ == "__main__":
    ft = FollowingTopic("chen-er-bai-18")
    for k, item in enumerate(ft.get_api_object()):
        print k, item['topic']['name']


