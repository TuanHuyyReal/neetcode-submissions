class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - l
        res = []
        while l < r and r <= len(nums):
            res.append(max(nums[l : r]))
            
            l += 1
            r += 1
        return res