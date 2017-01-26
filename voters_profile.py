#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/26
from zhihu_object import ZhiHuSpider
from pyquery import PyQuery as pq
from json import loads
class VotersProfile(ZhiHuSpider):
    def __init__(self,anwser_id):
        self._url = "https://www.zhihu.com/answer/{url_token}/voters_profile?total=55&offset={offset}"
        super(VotersProfile, self).__init__(self._url, anwser_id)

    def get_api_object(self):
        objects = loads(self._session.get(headers=self._headers, url=self.get_url()).text)

        if not self._totals:
            self._totals = int(objects["paging"]["total"])

        while self._current_numbers < self._totals:
            for item in objects["payload"]:
                _item = pq(item)
                item_info = pq(_item("a.zm-item-link-avatar"))
                yield dict(name=item_info.attr("title"),
                           url_token=item_info.attr("href").split("/")[-1])
            self._current_numbers += 10
            objects = loads(self._session.get(headers=self._headers, url=self.get_url()).text)

if __name__ == "__main__":
    vt = VotersProfile(52522003)
    for i, item in enumerate(vt.get_api_object()):
        print i, item