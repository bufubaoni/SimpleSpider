#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/20
class A(object):
    def __init__(self, a):
        self._a = a

    def q(self):
        print self._a


class B(A):
    def __init__(self,a):
        super(B, self).__init__(a)


if __name__ == "__main__":
    b = B("asldkfjaklsdflkj")
    b.q()
