class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        d = {}
        l = 0
        ans = 0
        for r in range(n):
            d[s[r]] = d.get(s[r], 0) + 1
            while d[s[r]] > 2:
                d[s[l]] -= 1
                if d[s[l]] ==0:
                    del d[s[l]]
                l+=1
            ans = max(ans, r-l+1)
        return ans