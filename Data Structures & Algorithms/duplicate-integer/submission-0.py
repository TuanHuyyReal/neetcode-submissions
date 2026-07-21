class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = []
        for i in nums:
            if i in a: return True
            a.append(i)
        return False