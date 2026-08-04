class Solution:
    def singleNumber(self, a: List[int]) -> int:
        ans = 0
        d = {}
        for i in a:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        for i in d:
            if d[i] ==1:
                ans = i
        return ans