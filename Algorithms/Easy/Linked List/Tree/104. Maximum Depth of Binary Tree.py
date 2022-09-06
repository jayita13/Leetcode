# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

''' Runtime: 76 ms, faster than 16.71% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.1 MB, less than 76.33% of Python3 online submissions for Maximum Depth of Binary Tree. '''
