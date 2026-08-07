class Solution:
    def addDigits(self, n: int) -> int:
        total = 0
        while n >= 10:
            n= sum(map(int,str(n)))
        return n
           
        
   
