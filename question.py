#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/26
from zhihu_object import ZhiHuSpider
from json import loads,dumps
from pyquery import PyQuery as pq
class Question(ZhiHuSpider):
    def __init__(self, question_id):
        self._url = "https://www.zhihu.com/node/QuestionAnswerListV2"
        self._html_url = "https://www.zhihu.com/question/{url_token}"
        super(Question, self).__init__(self._url, question_id)

    def get_url(self):
        return self._url

    def get_data(self):
        return dict(method="next",
                    params=dumps(dict(
                        url_token=self._url_token,
                        pagesize=10,
                        offset=self._current_numbers
                    )))

    def get_api_object(self):
        objects = pq(self._session.get(headers=self._headers, url=self._html_url.format(url_token=self._url_token)).text)

        if not self._totals:
            self._totals = int(objects("h3#zh-question-answer-num").attr("data-num"))
        objects = loads(self._session.post(headers=self._headers, data=self.get_data(), url=self.get_url()).text)
        while self._current_numbers < self._totals:
            for item in objects["msg"]:
                _item = pq(item)
                anwser = _item("div.zm-item-answer.zm-item-expanded")
                vote_info = _item("div.zm-votebar")
                content = _item("div.zm-item-rich-text>div.zm-editable-content.clearfix")
                anwser_info = _item("div.zm-item-answer-author-info>span>span>a.author-link")
                yield dict(anwser_id=anwser.attr("data-atoken"),
                           voteup_count=int(pq(vote_info)("span.count").text())if pq(vote_info)("span.count").text() else 0,
                           content=content.text(),
                           user_info=dict(url_token=anwser_info.attr("href").split("/")[-1] if anwser_info else None,
                                            name=anwser_info.text()))

            self._current_numbers += 10
            objects = loads(self._session.post(headers=self._headers, data=self.get_data(),url=self.get_url()).text)

if __name__ == "__main__":
    qus = Question(55314097)
    for item in qus.get_api_object():
        print item