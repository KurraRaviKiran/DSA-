class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                temp = (nums[i]-1)*(nums[j]-1)
                ans = max(ans,temp)
        return ans