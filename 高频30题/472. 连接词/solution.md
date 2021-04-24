思路:
思路一：字典树

把所有单词建成字典树，然后用DFS让每个单词在这课字典树上跑，看是否由多个单词组成

思路二： 用哈希

按单词长度递增排序

分布判断每个单词是否由前面单词短组成

判断方法有多种，还有一些优化！

代码都很好理解

代码:
思路一：
```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            if not word: continue
            cur = trie
            for w in word:
                cur = cur.setdefault(w, {})
            cur["#"] = "#"  # 结束标志
        res = []

        def dfs(word, idx, cnt, cur):
            if idx == len(word):
                # 组成个数 > 2, 并且以#结束的
                if cnt >= 1 and "#" in cur:
                    return True
                return False
            if "#" in cur:
                if dfs(word, idx, cnt + 1, trie):
                    return True
            if word[idx] not in cur:
                return False
            if dfs(word, idx + 1, cnt, cur[word[idx]]):
                return True
            return False

        for word in words:
            # 参数分别为, 单词word, 位置idx, 目前为止有几个单词组成了cnt, 字典树trie
            if dfs(word, 0, 0, trie):
                res.append(word)
        return res
```
边建立前缀树边check
```python

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def check_word(word, pre_dict):
            if len(word) == 0:
                return True
            cur_dict = pre_dict
            for index, c in enumerate(word):
                cur_dict = cur_dict.get(c, None)
                if cur_dict is None:
                    return False
                if cur_dict.get('end', 0) == 1:
                    # 当前字符串前缀与树中单词匹配，递归搜索
                    if check_word(word[index+1:], pre_dict):
                        return True
            return False
        
        words.sort(key=lambda x: len(x))
        ans = []
        pre_dict = {}
        for item in words:
            if len(item) == 0:
                continue
            if check_word(item, pre_dict):
                ans.append(item)
            else:
                # insert word
                cur_dict = pre_dict
                for c in item:
                    if cur_dict.get(c, None) is None:
                        cur_dict[c] = {}
                    cur_dict = cur_dict.get(c)
                cur_dict['end'] = 1
        return ans
```
```python
        words = sorted(words,key=lambda i:len(i))
        s = set(words)
        ans = []
        while words:
            word = words.pop(-1)
            s.remove(word)
            L = len(word)
            stack = [0]
            while stack:
                p = stack.pop(0)
                flag = False
                for i in range(p+1,L+1):
                    if word[p:i] in s:
                        stack.append(i)
                        if i == L:
                            ans.append(word)
                            flag = True
                            break
                if flag:break
        return ans
```

思路二
```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        min_len = max(1, len(words[0]))
        prev = set()
        res = []
 
        """
        方法1 动态规划方法判断
        def check(word, prev):
            if not prev: return False
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(i):
                    if not dp[j]: continue
                    if word[j:i] in prev:
                        dp[i] = True
                        break
            return dp[-1]
        """
        
        """
        # 方法2, DFS吧
        # def check(word):
        #     if not prev: return False
        #     if not word: return True
        #     for i in range(1, len(word) + 1):
        #         if word[:i] in prev and check(word[i:]):
        #             return True
        #     return False
        """
        # 方法3, 加了一个长度限制, 速度加快很多
        def check(word):
            if  word in prev: return True
            for i in range(min_len, len(word) - min_len + 1):
                if word[:i] in prev and check(word[i:]):
                    return True
            return False

        for word in words:
            if check(word):
                res.append(word)
            prev.add(word)
        return res
```