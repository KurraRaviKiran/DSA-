class Solution:
    def rotate(self, a: List[int], k: int) -> None:
        n = len(a)
        k = k%n
        temp = []
        for i in range(n-k,n):
            temp.append(a[i])
        for i in range(n-k-1, -1, -1):
            a[i+k] = a[i]
        for i in range(k):
            a[i] = temp[i]
        return a
                