#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/20
from pyquery import PyQuery as pq
from zhihu_object import ZhiHuSpider
from json import loads
import pdb


class Answers(ZhiHuSpider):
    def __init__(self, url, api_url):
        super(Answers, self).__init__(url, api_url)

    def get_objects(self):

        objects = pq(self.get_html())("div#data").attr("data-state")
        return objects

    def get_api_objects(self):
        _objects = loads(self.get_api_object())
        # print _objects
        return _objects["data"]


if __name__ == "__main__":
    aw = Answers(url="https://www.zhihu.com/people/chen-er-bai-18/answers",
                 api_url="https://www.zhihu.com/api/v4/members/chen-er-bai-18/answers?"
                         "include=data[*].is_normal,"
                         "suggest_edit,"
                         "comment_count,"
                         "collapsed_counts,"
                         "reviewing_comments_count,"
                         "can_comment,"
                         "content,"
                         "voteup_count,"
                         "reshipment_settings,"
                         "comment_permission,"
                         "mark_infos,created_time,"
                         "updated_time,"
                         "relationship.voting,"
                         "is_author,"
                         "is_thanked,"
                         "is_nothelp,"
                         "upvoted_followees;"
                         "data[*].author.badge[?(type=best_answerer)].topics&offset=20&limit=20&sort_by=created")

    for i, aw in enumerate(aw.get_api_objects()):
        print "{numb}: {aw}".format(numb=i, aw=aw["question"]["title"].encode("utf8"))
