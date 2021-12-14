class Solution:
    def search(self, nums, target: int):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int ((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
        return -1


s = Solution()
nums = [-1,0,3,5,9,12]
target = 2
print(s.search(nums, target))