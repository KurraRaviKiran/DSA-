class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        h = sum(nums)
        
        while l<=h:
            mid = (l+h )//2
            current_sum = 0
            count =1
            for i in range(len(nums)):
                if current_sum + nums[i] > mid:
                    count += 1
                    current_sum = nums[i]
                else:
                    current_sum += nums[i]

            if count > k:
                l= mid + 1
            else:
                h = mid - 1
        return l
