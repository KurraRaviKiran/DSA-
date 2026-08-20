class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        l =0
        r = len(a)-1
        while l<=r:
            mid= (l+r)//2
            missing = a[mid]-(mid+1)
            if missing <k:
                l = mid+1
            else:
                r = mid-1
        return r+1+k