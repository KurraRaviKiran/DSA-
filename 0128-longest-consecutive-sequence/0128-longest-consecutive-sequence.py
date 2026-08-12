class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        a.sort()
        longest = 0
        c = 0
        smallest = float("-inf")
        for i in range(len(a)):
            if a[i] -1 == smallest:
                c+=1
                smallest = a[i]
            elif a[i] != smallest:
                c=1
                smallest = a[i]
            longest = max(longest,c)
        return longest