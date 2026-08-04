class Solution:
    def findMissingElements(self, a: List[int]) -> List[int]:
        a.sort()
        l = []
        n = len(a)
        ans = float("-inf")
        m = float("inf")
        for i in range(n):
            m = min(m,a[i])
            ans = max(ans,a[i])
        for i in range(m,ans):
            if i not in a:
                l.append(i)
        return l