class Solution:
    def findMaxConsecutiveOnes(self, a: List[int]) -> int:
        ans = 0
        l = 0
        temp = 0
        n = len(a)
        for r in range(n):
            if a[r] ==1:
                temp+=1
            if a[r] != 1:
                temp = 0
            ans = max(ans,temp)
        return ans
        