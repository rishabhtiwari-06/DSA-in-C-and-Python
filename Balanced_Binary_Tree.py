#11
from typing import Optional

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_depth = check_balance(node.left)
            right_depth = check_balance(node.right)
            if left_depth ==-1 or right_depth == -1 or abs(left_depth - right_depth)>1:
                return -1
            return 1 + max(left_depth, right_depth)
        return check_balance(root) != -1
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    solution = Solution()
    result = solution.isBalanced(root)
    print("Tree is Symmetric?? ", result) 