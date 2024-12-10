from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Implement the inorder traversal function here
        result = []

        def inOrder(node: Optional[TreeNode]):
            if node is not None:
                inOrder(node.left)
                result.append(node.val)
                inOrder(node.right)
        inOrder(root)
        return result


# Example usage
if __name__ == "__main__":
    # Creating a sample tree: root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    result = solution.inorderTraversal(root)
    print("Inorder Traversal:", result)  # Expected output after implementing: [1, 3, 2]
