# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = [root.val]
        return self.inorderTraversal(root.left) + ans + self.inorderTraversal(root.right)
        
''' Runtime: 68 ms, faster than 5.20% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.7 MB, less than 96.97% of Python3 online submissions for Binary Tree Inorder Traversal. '''        
