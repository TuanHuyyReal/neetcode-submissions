class Solution:
    def dailyTemperatures(self, a: List[int]) -> List[int]:
        n = len(a)

        dp=[0]*(n)

        for i in range(n):
            for j in range(i+1, n):
                if a[i] < a[j]:
                    dp[i] = j-i
                    break

        return dp