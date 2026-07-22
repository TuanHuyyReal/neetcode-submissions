class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        i = 0
        if len(word2) > len(word1):
            while i < len(word2):
                if i < len(word1):
                    s+=word1[i]
                s+=word2[i]
                i +=1
        else:
            while i < len(word1):
                s += word1[i]
                if i < len(word2):
                    s+=word2[i]
                i += 1
        return s