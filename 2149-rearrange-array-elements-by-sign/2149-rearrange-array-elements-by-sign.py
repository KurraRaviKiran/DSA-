class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        f = []
        l = []
        for i in range(len(a)):
            if a[i] > 0:
                f.append(a[i])
            else:
                l.append(a[i])
        merged = []
        for pair in zip(f,l):
            for x in pair:
                merged.append(x)
        return merged

        