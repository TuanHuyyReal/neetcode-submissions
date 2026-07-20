class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        left = 0
        c = 0
        mc = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == nums[left]:
                c += 1
            else: #if nums[right] != nums[left]
                if c>mc:
                    res = nums[left]
                    mc = c
                c = 1
                left = right
            if right == len(nums) - 1:
                if c > mc:
                    res = nums[left]
        return res