class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for i in s:
            if 'A' <= i <= 'Z' or 'a' <= i <= 'z' or '0' <= i <= '9': a+=i.lower()
        left = 0
        right = len(a) - 1

        while left <= right:
            if a[left] != a[right]: return False
        
            left += 1
            right -=1
        
        return True