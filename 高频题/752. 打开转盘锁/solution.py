class Solution:
    def openLock(self, deadends, target: str) -> int:
        if "0000" in deadends:
            return -1
        a,b,c,d = list(target)
        return a,b,c,d


s = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(s.openLock(deadends,target)) 