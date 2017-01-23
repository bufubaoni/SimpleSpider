#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/23
from pydal import Field, DAL

db = DAL("sqlite://database/database.db")

db.define_table("followers",
                Field("name"),
                Field("url_token"),
                Field("follower_count"),
                Field("articles_count"),
                Field("answer_count"))

db.define_table("following",
                Field("name"),
                Field("url_token"),
                Field("follower_count"),
                Field("articles_count"),
                Field("answer_count"))

db.define_table("anwsers",
                Field("url_token"),
                Field("question"),
                Field("excerpt"),
                Field("content"),
                Field("voteup_count"))
