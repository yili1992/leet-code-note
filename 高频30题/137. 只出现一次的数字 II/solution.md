综述
该问题看起来很简单，使用 Set 或 HashMap 可以在 \mathcal{O}(N)O(N) 的时间和 \mathcal{O}(N)O(N) 的空间内解决。

真正的挑战在于 Google 面试官要求使用常数空间解决该问题（最近 6 个月该问题在 Google 上非常流行），测试应聘者是否熟练位操作。



方法一：HashSet
将输入数组存储到 HashSet，然后使用 HashSet 中数字和的三倍与数组之和比较。

3 \times (a + b + c) - (a + a + a + b + b + b + c) = 2 c
3×(a+b+c)−(a+a+a+b+b+b+c)=2c

```
class Solution:
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) // 2
```

复杂度分析

时间复杂度：\mathcal{O}(N)O(N)，遍历输入数组。

空间复杂度：\mathcal{O}(N)O(N)，存储 N/3N/3 个元素的集合。

方法二：HashMap
遍历输入数组，统计每个数字出现的次数，最后返回出现次数为 1 的数字。

```
from collections import Counter
class Solution:
    def singleNumber(self, nums):
        hashmap = Counter(nums)
            
        for k in hashmap.keys():
            if hashmap[k] == 1:
                return k
```
复杂度分析

时间复杂度：\mathcal{O}(N)O(N)，遍历输入数组。

空间复杂度：\mathcal{O}(N)O(N)，存储 N/3N/3 个元素的 Set。

方法三：位运算符：NOT，AND 和 XOR
思路

使用位运算符可以实现 \mathcal{O}(1)O(1) 的空间复杂度。

\sim x \qquad \textrm{表示} \qquad \textrm{位运算 NOT}
∼x表示位运算 NOT

x \& y \qquad \textrm{表示} \qquad \textrm{位运算 AND}
x&y表示位运算 AND

x \oplus y \qquad \textrm{表示} \qquad \textrm{位运算 XOR}
x⊕y表示位运算 XOR

XOR

该运算符用于检测出现奇数次的位：1、3、5 等。

0 与任何数 XOR 结果为该数。

0 \oplus x = x
0⊕x=x

两个相同的数 XOR 结果为 0。

x \oplus x = 0
x⊕x=0

以此类推，只有某个位置的数字出现奇数次时，该位的掩码才不为 0。

![](https://pic.leetcode-cn.com/Figures/137/xor.png)

因此，可以检测出出现一次的位和出现三次的位，但是要注意区分这两种情况。

AND 和 NOT

为了区分出现一次的数字和出现三次的数字，使用两个位掩码：seen_once 和 seen_twice。

思路是：

仅当 seen_twice 未变时，改变 seen_once。

仅当 seen_once 未变时，改变seen_twice。


![](https://pic.leetcode-cn.com/Figures/137/three.png)
位掩码 seen_once 仅保留出现一次的数字，不保留出现三次的数字。


```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        
        for num in nums:
            # first appearance: 
            # add num to seen_once 
            # don't add to seen_twice because of presence in seen_once
            
            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice
            
            # third appearance: 
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once
```
复杂度分析

时间复杂度：\mathcal{O}(N)O(N)，遍历输入数组。

空间复杂度：\mathcal{O}(1)O(1)，不使用额外空间。