class Solution:
    def findAnagrams(self, s: str, p: str):
        left, right = 0, 0
        result = []
        size = len(p)
        count = [0] * 26
        windows = [0] * 26
        for i in range(size):
            count[ord(p[i]) - 97] += 1
        if len(s) < size:
            return result
        while right < len(s):
            right += 1
            windows[ord(s[right - 1]) - 97] += 1
            if windows == count:
                result.append(left)
            while right - left >= size:
                windows[ord(s[left]) - 97] -= 1
                left += 1
        return result


s = Solution()
t = "ababababab"
p = "aab"
print(s.findAnagrams(t, p))