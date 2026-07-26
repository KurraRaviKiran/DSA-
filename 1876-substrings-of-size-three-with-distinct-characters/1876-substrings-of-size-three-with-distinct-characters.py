class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        n = len(s)
        ans = 0
        temp = []
        for r in range(n):
            temp.append(s[r])
            if (r-l == 3):
                temp.pop(0)
                l+=1
            if (r-l+1 == 3) and len(set(temp)) == 3:
                ans+=1

        return ans