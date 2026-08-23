class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}

        for i in s:
            d[i] = d.get(i, 0) + 1

        ans = ""

        for char, freq in sorted(d.items(), key=lambda x: x[1], reverse=True):
            ans += char * freq

        return ans