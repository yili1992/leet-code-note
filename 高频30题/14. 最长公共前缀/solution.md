思路一 ：滑动窗口（双指针）
题目中要求答案必须是 子串 的长度，意味着子串内的字符在原字符串中一定是连续的。因此我们可以将答案看作原字符串的一个滑动窗口，并维护窗口内不能有重复字符，同时更新窗口的最大值。
![](https://pic.leetcode-cn.com/ce96f9b99cba13a8c9f8b9c28d56b2e055fcc4186d9f36475674a673f9798fdc-TIM%E6%88%AA%E5%9B%BE20200224210256.png)



算法
初始化头尾指针 head，tail；
tail 指针右移，判断 tail 指向的元素是否在 [head:tail] 的窗口内；
如果窗口中没有该元素，则将该元素加入窗口，同时更新窗口长度最大值，tail 指针继续右移；
如果窗口中存在该元素，则将 head 指针右移，直到窗口中不包含该元素。
返回窗口长度的最大值。

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        tail = 0
        if len(s) < 2: return len(s) # 边界条件
        res = 1
        
        while tail < len(s) - 1:
            tail += 1
            if s[tail] not in s[head: tail]:
                res = max(tail - head + 1, res)
            else:
                while s[tail] in s[head: tail]:
                    head += 1
        return res
```
复杂度分析
时间复杂度：\mathcal{O}(n^2)O(n 
2
 )。
空间复杂度：\mathcal{O}(1)O(1)，使用了 head，tail，res。


思路二：优化的滑动窗口（哈希表）
我们可以使用哈希表记录每个字符的下一个索引，然后尽量向右移动尾指针来拓展窗口，并更新窗口的最大长度。如果尾指针指向的元素重复，则将头指针直接移动到窗口中重复元素的右侧。

算法
tail 指针向末尾方向移动；
如果尾指针指向的元素存在于哈希表中：
head 指针跳跃到重复字符的下一位；
更新哈希表和窗口长度。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashmap = {}
        head, res = 0, 0
        for tail in range(n):
            if s[tail] in hashmap:
                head = max(hashmap[s[tail]], head)
            hashmap[s[tail]] = tail + 1
            res = max(res, tail - head + 1)
        return res
复杂度分析
时间复杂度：\mathcal{O}(n)O(n)，遍历了一遍 s，哈希表中查找的时间复杂度为 \mathcal{O}(1)O(1)。
空间复杂度：\mathcal{O}(n)O(n)，使用了哈希表。
