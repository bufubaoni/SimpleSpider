#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/20
from pyquery import PyQuery as pq
from zhihu_object import ZhiHuSpider
from json import loads
import pdb


class Answers(ZhiHuSpider):
    def __init__(self, url):
        super(Answers, self).__init__(url)



if __name__ == "__main__":
    aw = Answers(url="https://www.zhihu.com/api/v4/members/chen-er-bai-18/answers?"
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
                         "data[*].author.badge[?(type=best_answerer)].topics&offset={offset}&limit=20&sort_by=created")

    for i in aw.get_api_object():
        print i
        # for q in i:
        # print i["question"]["title"]
