#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2021/7/6 4:00 下午
@desc:
"""
import threading

lock = threading.Lock()


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        lock.acquire()
        if not hasattr(Singleton, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        lock.release()
        return cls._instance


if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    print(id(a))
    print(id(b))