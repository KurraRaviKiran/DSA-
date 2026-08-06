class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        a = s.split()
        r= len(a) -1
        while l<=r:
            a[l],a[r] = a[r],a[l]
            l+=1
            r-=1
        s = " ".join(a)
        return s.strip(" ")