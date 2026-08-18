class Solution:
    def largestInteger(self, a: List[int], k: int) -> int:
        ans = -1
        d= {}
        for i in range(len(a)):
            temp = []
            for j in range(i,len(a)):
                temp.append(a[j])
                if len(temp)==k:
                    for m in set(temp):
                        if m not in d:
                            d[m]=1
                        else:
                            d[m]+=1
                    break
        for m in d:
            if d[m]==1:
                ans = max(ans,m)
        return ans
        