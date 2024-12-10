#15
from typing import Optional

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverseInOrder(self, root):
        if root is not None:
            self.traverseInOrder(root.left)
            print(root.val)
            self.traverseInOrder(root.right)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
       def dfs ( node , current_number):
           if not node:
               return 0
           current_number = current_number *10 + node.val
           if not node.left and not node.right:
               return current_number
           left_sum = dfs(node.left, current_number)
           right_sum = dfs(node.right, current_number)
           return left_sum + right_sum
       return dfs(root , 0)
if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    root.right = TreeNode(0)

    solution = Solution()
    result = solution.sumNumbers(root)
    print("Sum: ",result)
    solution.traverseInOrder(root)