#24
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key< root.val:
            root.left = self.deleteNode(root.left,key)
        elif key> root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right,successor.val)
        return root
            
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
            
    def traverseInOrder(self, root):
        if root is not None:
            self.traverseInOrder(root.left)
            print(root.val)
            self.traverseInOrder(root.right)


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    key = 2
    sol = Solution()
    res= sol.deleteNode(root, key)
    sol.traverseInOrder(root)
    # print("Kth Smallest is :", res)
