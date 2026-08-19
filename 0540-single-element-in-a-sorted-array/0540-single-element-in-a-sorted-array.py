class Solution:
    def singleNonDuplicate(self, a: List[int]) -> int:
        d = {}
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]==1:
                temp = i
        return temp