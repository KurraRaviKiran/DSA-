class Solution:
    def singleNonDuplicate(self, a: List[int]) -> int:
        l = 1
        n = len(a)
        h = n-2
        if n == 1:
            return a[0]
        if a[0] != a[1]:
            return a[0]
        if a[n-1] != a[n-2]:
            return a[n-1]
        while l<=h:
            mid =(l+h)//2
            if a[mid] != a[mid-1] and a[mid] != a[mid+1]:
                return a[mid]
            if mid%2==1 and a[mid] ==a[mid-1] or mid%2==0 and a[mid] == a[mid+1]:
                l = mid+1
            else:
                h = mid-1
        return -1