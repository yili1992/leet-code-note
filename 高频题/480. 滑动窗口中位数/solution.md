前言
本题和 295. 数据流的中位数 非常相似。
求 a 的中位数的思路与代码如下：

python3思路

(a[(len(a)-1)//2] + a[len(a)//2]) / 2
解法一：数组+暴力法
这个办法不难想到，就是将每一组的中位数加入返回结果res，再返回。

第一种
执行用时：4992 ms，在所有 Python3 提交中击败了 25.46% 的用户
内存消耗：16.1 MB，在所有 Python3 提交中击败了 42.07% 的用户

第二种
执行用时：7248 ms，在所有 Python3 提交中击败了 5.09% 的用户
内存消耗：16.4 MB，在所有 Python3 提交中击败了 14.02% 的用户

```python

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = lambda a: (a[(len(a)-1)//2] + a[len(a)//2]) / 2
        res = []
        for i in range(len(nums)-k+1):
            res.append(median(sorted(nums[i:i+k])))
        return res
```
时间复杂度
时间复杂度：O(n k log k)O(nklogk)，排序的时间复杂度为O(k log k)O(klogk)，总共执行了 nn 次。

解法二：数组+二分查找
维护一个数组 a，它保存当前数组，最开始等于排好序的 nums 的前 k 个元素。注意：a 是排好序的。
用 res 保存返回结果，首先将a加入。
用 i, j 循环 nums，它们分别表示删除值和加入值，每一对 i, j 都要执行下面步骤：
将 a 中值为 i 的元素删除；
将 j 增加在合适的位置，使用二分查找库（bisect）；
得到中位数并增加到 res 的最后。
返回。
举例
输入：nums = [1, 3, -1, -3, 5], k = 2
步骤：

a = [1, 3]，res = [a的中位数] = [2]
a = [1, 3]，删除1，增加-1，a = [-1, 3]，res增加a的中位数 = 1，res = [2, 1]
a = [-1, 3]，删除3，增加-3，a = [-3, -1]，res增加a的中位数 = -2，res = [2, 1, -2]
a = [-3, -1]，删除-1，增加5，a = [-3, 5]，res增加a的中位数 = 1，res = [2, 1, -2, 1]
返回res
执行结果
执行用时：308 ms，在所有 Python3 提交中击败了 38.91% 的用户
内存消耗：16.1 MB，在所有 Python3 提交中击败了 43.91% 的用户

```python

import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = lambda a: (a[(len(a)-1)//2] + a[len(a)//2]) / 2
        a = sorted(nums[:k])
        res = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            a.remove(i)
            bisect.insort_left(a, j)
            res.append(median(a))
        return res
```
时间复杂度
时间复杂度：O(nk)O(nk)

解法三：数组+二分查找（优化）
和解法二思路一致，思路改变部分加粗了，思路如下：

维护一个数组 a，它保存当前数组，最开始等于排好序的 nums 的前 k 个元素。注意：a 是排好序的。
用 res 保存返回结果，首先将 a 加入。
用 i, j 循环 nums，它们分别表示删除值和加入值，每一对 i, j 都要执行下面步骤：
将值为 i 的索引从 a 中删除，使用二分查找库（bisect）；
将j增加在合适的位置，使用二分查找库（bisect）；
得到中位数并增加到 res 的最后。
返回。
执行结果
执行用时：72 ms，在所有 Python3 提交中击败了 100.00% 的用户
内存消耗：16.1 MB，在所有 Python3 提交中击败了 44.28% 的用户

```python

import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = lambda a: (a[(len(a)-1)//2] + a[len(a)//2]) / 2
        a = sorted(nums[:k])
        res = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            a.pop(bisect.bisect_left(a, i))
            bisect.insort_left(a, j)
            res.append(median(a))
        return res
```
时间复杂度
时间复杂度：O(nk)O(nk)
