### 思路：把字符串看错一个小人跳动的过程，字典内的单词看作小人跳跃的规则。

把小人能够跳跃的过程作为路径，查看所有可能的路径，如果有一条路径能够达到最后，则表示能够拆分。

比如：s="leetcode",wordDict=["leet","code"] 可以看作小人从'l'的左边一位空位' '，跳跃至't'，后跳跃至'e'。

我们使用动态规划模拟这一过程。
DP=[True,False,False,False,False,False,False,False,False],字符串为8位，DP为9位。
```
首先，s[0:4]=='leet' 是wordDict内的单词，所以dp[4]=True。
继续以0为起点，4以后的索引为终点的单词都不在字典内，选择忽略。
即'leetc','leetco','leetcod','leetcode'都不在字典内，忽略不管。

第二步，因为之前设置了DP[4]=True,所以迭代至4为起点
查看后面的单词是否在字典内。发现s[4:8]=='code' 在字典内，
所以设置DP[8]为True，至此循环结束。
返回DP[-1] 若是True，则表示能够拆分
```
第二个例子 s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
```
DP=[True,False,False,False,False,False,False,False,False，False]

第一步，以0为起点迭代，得到'cat'，'cats'都在字典内，则
DP=[True,False,False,True,True,False,False,False,False，False]
第二步，以3为起点迭代，得到'sand'在字典内，则dp[7]=True
DP=[True,False,False,True,True,False,False,True,False，False]
第三步，以4为起点迭代，'and'在字典内,则dp[7]=True。
DP=[True,False,False,True,True,False,False,True,False，False]
第四步，以7为起点迭代，未得到单词在字典内。
结束
返回 dp[-1]为False
```