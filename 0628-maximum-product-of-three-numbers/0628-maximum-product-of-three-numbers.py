class Solution:
    def maximumProduct(self, a: List[int]) -> int:
        a.sort()
        p1 = a[-1]*a[-2]*a[-3]
        p2 = a[0]*a[1]*a[-1]
        ans = max(p1,p2)
        return ans
      
    