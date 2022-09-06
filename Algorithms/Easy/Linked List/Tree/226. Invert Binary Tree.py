# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        
        return root
        
''' Runtime: 53 ms, faster than 23.95% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.9 MB, less than 11.96% of Python3 online submissions for Invert Binary Tree. '''       
