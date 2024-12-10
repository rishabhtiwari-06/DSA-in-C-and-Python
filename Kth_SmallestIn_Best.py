#24
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            
            current = current.right
            current = current.right


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    # root.right.left = TreeNode(7)
    # root.right.right = TreeNode(10)
    k = 2
    sol = Solution()
    res = sol.kthSmallest(root, k)
    print("Kth Smallest is :", res)
