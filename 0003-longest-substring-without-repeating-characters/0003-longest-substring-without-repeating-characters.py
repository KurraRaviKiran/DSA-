class Solution:
    def lengthOfLongestSubstring(self, a: str) -> int:
        l = 0
        ans  = 0
        n = len(a)
        s = set()
        for r in range(n):
            if a[r] not in s:
                s.add(a[r])
            else:
                while a[r] in s:
                    s.remove(a[l])
                    l+=1
                s.add(a[r])
            ans = max(ans,r-l+1)

        return ans