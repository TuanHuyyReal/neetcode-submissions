class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for i in nums:
            if i not in a: a[i] = 1
            else: return True
        return False