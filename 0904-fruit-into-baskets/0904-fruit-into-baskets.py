class Solution:
    def totalFruit(self, a: List[int]) -> int:
        l = 0
        d = {}
        ans = 0
        n = len(a)
        for r in range(n):
            if a[r] not in d:
                d[a[r]] =1
            else:
                d[a[r]]+=1

            while len(d) > 2:
                lval = a[l]
                d[lval] -=1
                if d[lval] ==0:
                    d.pop(lval)
                l+=1
            ans = max(ans,r-l+1)
        return ans