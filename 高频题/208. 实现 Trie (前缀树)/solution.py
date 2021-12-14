#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.trie
        for index, i in enumerate(word):
            if index == len(word) - 1:
                if not cur.get(i, None):
                    cur[i] = {'#': None}
                else:
                    cur[i]['#'] = None
            else:
                cur = cur.setdefault(i, {})

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        result = False
        cur = self.trie
        for i in word:
            cur = cur.get(i, None)
            if not cur:
                break
        else:
            if '#' in cur.keys():
                result = True
        return result


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        result = False
        cur = self.trie
        for i in prefix:
            cur = cur.get(i, None)
            if not cur:
                break
        else:
            result = True
        return result




# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("app")
param_3 = obj.startsWith("app")
print(param_2)
print(param_3)
obj.insert("app")
print(obj.trie)
print(obj.search("app"))