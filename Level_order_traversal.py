#18
from typing import Optional

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self,root):
        q =[]
        q.append(root)
        while len(q) !=0:
            root = q.pop(0)
            print(root.val, end= " ")
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)      

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(9)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(10)

    sol = Solution()
    sol.levelOrder(root)