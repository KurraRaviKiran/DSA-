class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort()
        ans = []
        m= float('inf')
        n = len(a)
        l = 0
        for r in range(n):
            if (r-l==2):
                l+=1
            if (r-l+1==2):
                diff = a[r]- a[l]
                if diff < m:
                    m = diff
                    ans = [[a[l], a[r]]]
                elif ( diff== m):
                    ans.append([a[l], a[r]])
        return ans