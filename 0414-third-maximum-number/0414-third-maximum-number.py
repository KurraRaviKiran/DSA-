class Solution:
    def thirdMax(self, a: List[int]) -> int:
        large = float("-inf")
        second =float("-inf")
        third = float("-inf")
        for i in a:
            if i > large:
                third = second
                second = large
                large  = i
            elif i > second and i != large:
                third = second
                second = i
            elif i > third and i != second and i !=large:
                third = i
        if third in a:
            return third
        else:
            return large