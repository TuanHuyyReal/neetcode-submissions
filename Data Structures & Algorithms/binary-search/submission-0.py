class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r and r <= len(nums) - 1:
            g = (l+r)//2
            if nums[g] < target: l = g + 1
            if nums[g] > target: r = g - 1
            elif nums[g] == target: return g
        return -1