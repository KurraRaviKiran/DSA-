class Solution:
    def numOfSubarrays(self, a: List[int], k: int, threshold: int) -> int:
        n = len(a)
        v = 0
        l = 0
        temp = 0
        for r in range(n):
            temp +=a[r]
            if (r-l ==k):
                temp-=a[l]
                l+=1
            if (r-l+1==k):
                if temp/k >= threshold:
                    v +=1
        return v