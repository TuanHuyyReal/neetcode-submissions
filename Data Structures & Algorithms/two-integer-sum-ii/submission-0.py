class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a,b = 0,0

        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] == numbers[j]: continue
                if numbers[i] + numbers[j] == target:
                    a = min(i,j) + 1
                    b = max(i,j) + 1

        return [a,b]