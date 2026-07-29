class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        l = 0
        temp = 0
        ans = 0
        n= len(a)
        for r in range(n):
            if a[r]==0:
                temp +=1
            while temp >k:
                if a[l] ==0:
                    temp-=1
                l+=1
            ans = max(ans,r-l+1)
        return ans