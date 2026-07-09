class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # the number of rows 
        n = len(matrix[0]) # the number of items in each list
        L, R = 0, (m*n)-1

        while L <= R:
            mid = (L+R) //2
            row, col = mid//n, mid%n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:  # value too small → target is bigger → search right
                L = mid + 1
            else:
                R = mid - 1
        
        return False