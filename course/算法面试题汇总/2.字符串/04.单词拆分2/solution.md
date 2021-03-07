### 思路：使用回溯(dfs)
这里使用跟2.02分割回文串里的 回溯法中的dfs就能解决，但是在提交的时候有个特殊的例子
```
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
```
会导致执行超时
因此这里要先判断s能不能被分割，使用2.03单测拆分里的判断，如果不能拆分则直接返回。
但是我这样的写法耗时耗内存，还可以继续优化