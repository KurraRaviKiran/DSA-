class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1+nums2
        l.sort()
        mid = len(l)//2
        if len(l)%2==0:
            ans = (l[mid] + l[mid-1])/2
        else:
            ans = l[mid]
        return ans