class Solution:
    def minimumDifference(self, a: List[int], k: int) -> int:
        a.sort()
        ans = float('inf')
        l = 0
        for r in range(len(a)):
            if (r-l == k ):
                l+=1
            if (r-l+1 == k):
                ans = min(ans,a[r]-a[l])
        return ans