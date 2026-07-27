class Solution:
    def minimumCost(self, c: List[int]) -> int:
        c.sort()
        n = len(c)
        took = 0
        temp = 0
        for i in range(n-1,-1,-1):
            if took == 2:
                took = 0
            else:
                temp = temp + c[i]
                took +=1
        return temp