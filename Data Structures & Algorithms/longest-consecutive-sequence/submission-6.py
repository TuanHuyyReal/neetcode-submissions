class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0;

        arr = sorted(list(set(nums)))

        longest = 1
        curr = 1
        last = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - 1 == last:
                curr +=1
            else:
                longest = max(longest, curr)
                curr = 1
            if i == len(arr) - 1 and arr[i] - 1 == last: longest = max(longest, curr)
            last = arr[i]

        return longest