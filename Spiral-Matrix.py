# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result

        top, bot, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bot and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse from top to bot along the right column
            for i in range(top, bot + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse from right to left along the bot row
            if top <= bot:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bot][i])
                bot -= 1

            # Traverse from bot to top along the left column
            if left <= right:
                for i in range(bot, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()

    # Example matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Spiral Order of matrix:", sol.spiralOrder(matrix))
