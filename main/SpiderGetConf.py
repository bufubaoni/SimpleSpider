#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple

Section = namedtuple("Section", ["name", "content"])
import re


class SpiderGetConf(object):
    def __init__(self, path):
        self._path = path
        self._file = open(path, "r")
        self._Sections = self.getSection()

    def getFile(self):
        pass

    def getConfig(self):
        Sections = list()
        count_section=0
        for section in self._Sections:
            if section.name == "headers":
                Sections.append(Section(section.name, dict()))
                count_section += 1
                Sections[count_section-1].content.update (
                    {line.split(":")[0].strip(): line.split(":")[1].strip()
                     for line in section.content})
        return Sections

    def getSection(self):
        re_section = "\[(.+)\]"
        Sections = list()
        count_section = 0
        for line in self._file.readlines():
            section_name = re.findall(re_section, line)
            if section_name:
                section = Section(section_name[0], list())
                Sections.append(section)
                count_section += 1
            else:
                Sections[count_section - 1].content.append(line)
        return Sections

    def getContent(self):
        pass


if __name__ == "__main__":
    testconf=SpiderGetConf("conf/first.conf")
    print(testconf.getConfig())