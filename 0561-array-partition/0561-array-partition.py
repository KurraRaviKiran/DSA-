class Solution:
    def arrayPairSum(self, a: List[int]) -> int:
        a.sort()
        temp = 0
        for i in range(0,len(a),2):
            temp+= a[i]
        return temp

        