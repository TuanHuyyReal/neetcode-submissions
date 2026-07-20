class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]

        s = [[1],[1,1]]
        for i in range(2, numRows):
            a = [1]
            for j in range(1,len(s[i-1])):
                a.append(s[i-1][j-1] + s[i-1][j])
            s.append(a+[1])
        return s