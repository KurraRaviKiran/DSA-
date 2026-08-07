class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        ans = ""
        for i in t:
            if i not in d:
                ans = i
                break
            else:
                d[i]-=1
                if d[i] <0:
                    ans = i
                    break
        return ans