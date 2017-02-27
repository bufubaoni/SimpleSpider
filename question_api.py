#!/usr/bin/env python
# -*- coding: utf-8 -*-
# zhihu.com update there api
from zhihu_object import ZhiHuSpider


class Question(ZhiHuSpider):
    def __init__(self, url_token):
        self._url = ("https://www.zhihu.com/api/v4/questions/{url_token}/answers?"
                     "sort=default&"
                     "include=data[*].is_normal,"
                     "is_sticky,"
                     "collapsed_by,"
                     "suggest_edit,"
                     "comment_count,"
                     "collapsed_counts,"
                     "reviewing_comments_count,"
                     "can_comment,"
                     "content,"
                     "editable_content,"
                     "voteup_count,"
                     "reshipment_settings,"
                     "comment_permission,"
                     "mark_infos,"
                     "created_time,"
                     "updated_time,"
                     "relationship.is_author,"
                     "voting,"
                     "is_thanked,"
                     "is_nothelp,"
                     "upvoted_followees;"
                     "data[*].author.is_blocking,"
                     "is_blocked,"
                     "is_followed,"
                     "voteup_count,"
                     "message_thread_token,"
                     "badge[?(type=best_answerer)].topics&"
                     "limit=20&"
                     "offset={offset}")
        super(Question, self).__init__(self._url, url_token)

if __name__ == "__main__":
    qus = Question(35104003)
    for item in qus.get_api_object():
        print item

