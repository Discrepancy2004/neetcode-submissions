class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = matrix
        n1 = len(matrix)
        n2 = len(matrix[0])
        for i in range(n1):
            if matrix[i][-1] == target:
                return True
            elif matrix[i][-1] >= target:
                
                    l = 0
                    r = n2-1

                    while(l<=r):
                        mid = l + (r-l)//2

                        if target == matrix[i][mid]:
                            return True
                        elif target < matrix[i][mid]:
                            r = mid - 1
                        elif target > matrix[i][mid]:
                            l = mid + 1

                    return False
            
        
        return False

                        