class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        low, high = 0, m-1

        while low <= high:
            row = low + (high-low) // 2

            # if nums[mid] == target:
            #     return True
            # elif nums[mid] < target:
            #     low = mid

            if target > matrix[row][n-1]:
                low = row + 1
            elif target < matrix[row][0]:
                high = row - 1
            else:
                break

        if not (low <= high): return False

        l,r = 0, n-1 

        while l<=r:
            m=(l+r)// 2
            if target > matrix[row][m]:
                l= m+1
            elif target < matrix[row][m]:
                r= m-1
            else:
                return True
        return False



        