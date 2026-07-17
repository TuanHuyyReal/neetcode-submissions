class Solution:
    def maxArea(self, heights: List[int]) -> int:
        dp = [0]*(len(heights))

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                dp[i] = max(dp[i], min(heights[i], heights[j])*(j-i))

        return max(dp)