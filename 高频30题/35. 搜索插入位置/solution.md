二分查找的核心思想
二分查找的核心思想是「减而治之」，即「不断缩小问题规模」。

思路 2：在循环体内部排除元素（重点）
while(left < right) 这种写法表示在循环体内部排除元素；
退出循环的时候 left 和 right 重合，区间 [left, right] 只剩下成 11 个元素，这个元素 有可能 就是我们要找的元素。
![](https://pic.leetcode-cn.com/1598340841-tpXMfu-file_1598340837988)

第 2 种思路可以归纳为「左右边界向中间走，两边夹」，这种思路在解决复杂问题的时候，可以使得思考的过程变得简单。

使用思路 2 完成「力扣」第 35 题
思路分析：

首先，插入位置有可能在数组的末尾（题目中的示例 3），需要单独判断。如果在数组的末尾，插入位置的下标就是数组的长度；
否则，根据示例和暴力解法的分析，插入位置的下标是 大于等于 target 的第 11 个元素的位置。
因此，严格小于 target 的元素一定不是解，在循环体中将左右边界 left 和 right 逐渐向中间靠拢，最后 left 和 right 相遇，则找到了插入元素的位置。根据这个思路，可以写出如下代码。

参考代码 1：

```
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return 0

        # 特判
        if nums[size - 1] < target:
            return size

        left = 0
        right = size - 1

        while left < right:
            # left + right 在 Python 中如果发生整型溢出，Python 会自动转成长整形
            mid = (left + right) // 2
            # 严格小于 target 的元素一定不是解
            if nums[mid] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            else:
                # 下一轮搜索区间是 [left, mid]
                right = mid
        return left
```
复杂度分析：

时间复杂度：O(\log N)O(logN)，这里 NN 是数组的长度，每一次都将问题的规模缩减为原来的一半，因此时间复杂度是对数级别的；
空间复杂度：O(1)O(1)，使用到常数个临时变量。
