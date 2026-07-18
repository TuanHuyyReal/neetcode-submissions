class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = -1

        row_left = 0
        row_right = len(matrix) - 1

        while row_left <= row_right:
            row_mid = (row_left + row_right)//2
            
            col_left = 0
            col_right = len(matrix[row_mid]) - 1

            min_v = matrix[row_mid][0]
            max_v = matrix[row_mid][-1]

            if min_v > target: 
                row_right = row_mid - 1
                continue
            if max_v < target:
                row_left = row_mid + 1
                continue

            while col_left <= col_right:
                col_mid = (col_left + col_right)//2

                if matrix[row_mid][col_mid] > target: col_right = col_mid - 1
                elif matrix[row_mid][col_mid] < target: col_left = col_mid + 1
                else: return True
            
            break
                
        return False