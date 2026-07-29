class Solution:
    def maxConsecutiveAnswers(self, a: str, k: int) -> int:
        l = 0
        temp = 0
        pump = 0
        ans = 0
        n= len(a)
        for r in range(n):
            if a[r]=="F":
                temp +=1
            if a[r] == "T":
                pump +=1
            while min(temp,pump) >k:
                if a[l] == "F":
                    temp-=1
                else:
                    pump -=1
                l+=1
            ans = max(ans,r-l+1)
        return ans