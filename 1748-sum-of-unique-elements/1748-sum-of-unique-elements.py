class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d= {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans = 0
        for i in d:
            if d[i] ==1:
                ans = ans + i
        return ans