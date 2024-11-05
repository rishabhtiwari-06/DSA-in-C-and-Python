from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = None
        self.val=val
        self.right=None

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return ((p.val == q.val) and (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right)))
        

if __name__ == "__main__":
    p = TreeNode(1)
    p.right = TreeNode(2)
    p.right.left = TreeNode(3)

    q = TreeNode(1)
    q.right = TreeNode(2)
    q.right.left = TreeNode(3)
    solution = Solution()
    result = solution.isSameTree(p,q)
    print("They Are Same:", result) 