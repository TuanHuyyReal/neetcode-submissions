class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        for i in nums:
            if i not in a: a[i] = 1
            else: a[i] += 1
        return list(reversed(sorted(a, key=lambda x: a[x])))[0:k]