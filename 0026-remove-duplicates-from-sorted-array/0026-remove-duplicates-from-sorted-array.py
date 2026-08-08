class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        l = []
        ans = 0
        for i in range(len(a)):
            if a[i] not in l:
                l.append(a[i])
                a[ans] = a[i]
                ans = ans + 1
        return ans