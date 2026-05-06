class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        totalLength = rows * columns
        l, r = 0, totalLength - 1
        while l <= r:
            mid = l + (r-l) //2
            # covert to the value at mid
            row = mid // columns
            column = mid % columns

            midValue = matrix[row][column]
            if midValue > target:
                r = mid - 1
            elif midValue < target:
                l = mid + 1
            else:
                return True
        return False
