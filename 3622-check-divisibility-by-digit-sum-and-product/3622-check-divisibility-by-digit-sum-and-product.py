class Solution:
    def checkDivisibility(self, n: int) -> bool:
        k = str(n)
        s = 0
        for i in k:
            temp = int(i)
            s = s+temp
        r = 1
        for i in k:
            m = int(i)
            r = r*m
        ans = s+r
        val = False
        if n%ans==0:
            val = True
        return val