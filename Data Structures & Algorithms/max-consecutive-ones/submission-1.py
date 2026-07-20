class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        res = 0
        for i in nums:
            if i == 1: c+=1
            else: 
                res = max(res, c)
                c = 0
        return max(res,  c)