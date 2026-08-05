class Solution:
    def search(self, a: List[int], target: int) -> int:
        low = 0
        ans = -1
        high = len(a)-1
        while low<= high:
            mid = (low+high)//2
            if a[mid] == target:
                ans = mid
                break
            elif target > a[mid]:
                low = mid+1
            else:
                high = mid-1
        return ans