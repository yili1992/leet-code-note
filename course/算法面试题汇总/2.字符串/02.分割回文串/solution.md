### 思路
方法——回溯  
![img](https://pic.leetcode-cn.com/1604822955-WbvWRE-131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.png)  
根据下标截取字符串，然后再从剩余的字符串中再截取，利用这种决策树思想构建递归函数求解。
此外，利用双指针判断回文串。

### 回溯算法
回溯算法是有递归的，纯暴力的搜索，主要是为了解决以下问题
- 组合问题， 比如1234 有哪些组合
- 切割问题
- 子集问题
- 排列问题
- 棋盘问题  

通常把集合 抽象为二叉树， 树的横方向是 集合的长度，纵向由递归处理。  
这个递归函数通常没有返回。

```python
def backchecking():
    if (条件){
        收集结果
        return
    }
    # 单层搜索逻辑
    for(遍历集合的每个元素){
        处理节点
        递归函数
        回溯操作(撤销操作, 回到上个情况 pop())
    }
    return 

```

### 回溯2
115 题 中考虑了分治、回溯、动态规划，这道题同样可以用回溯法。

回溯法其实就是一个 dfs 的过程，同样举个例子。

```
aabb
先考虑在第 1 个位置切割，a | abb
把 a 加入到结果中 [a]

然后考虑 abb
先考虑在第 1 个位置切割，a | bb
把 a  加入到结果中 [a a]

然后考虑 bb
先考虑在第 1 个位置切割，b | b
把 b 加入到结果中 [a a b] 

然后考虑 b
先考虑在第 1 个位置切割，b | 
把 b 加入到结果中 [a a b b] 

然后考虑空串
把结果加到最终结果中 [[a a b b]]

回溯到上一层 
考虑 bb
考虑在第 2 个位置切割，bb |
把 bb 加入到结果中 [a a bb] 

然后考虑 空串
把结果加到最终结果中 [[a a b b] [a a bb]]

然后继续回溯
```
可以看做下边的图做 dfs ，而每一层其实就是当前字符串所有可能的回文子串。

![img2](https://pic.leetcode-cn.com/3d757955a494533faaa83729fcd3be4d545438014018b70254655aa11ca794c9.jpg)

就是很经典的回溯法，一个 for 循环，添加元素，递归，删除元素。这里判断是否是回文串，我们就直接用 dp 数组。

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        #判断是否是回文串
        def pending_s(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        #回溯函数，这里的index作为遍历到的索引位置，也作为终止判断的条件
        def back_track(s, index):
            #如果对整个字符串遍历完成，并且走到了这一步，则直接加入result
            if index == len(s):
                result.append(path[:])
                return
            #遍历每个子串 
            for i in range(index, len(s)):
                #剪枝，因为要求每个元素都是回文串，那么我们只对回文串进行递归，不是回文串的部分直接不care它
                #当前子串是回文串
                if pending_s(s[index : i + 1]):
                    #加入当前子串到path
                    path.append(s[index: i + 1])
                    #从当前i+1处重复递归
                    back_track(s, i + 1)
                    #回溯
                    path.pop()
        back_track(s, 0)
        return result
```
p
