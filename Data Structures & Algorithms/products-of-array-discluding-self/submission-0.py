class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                output[i]*=nums[j] if j != i else 1
            
        return output