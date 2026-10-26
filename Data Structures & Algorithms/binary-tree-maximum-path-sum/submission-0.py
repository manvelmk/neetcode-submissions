# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_sum = 0 
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> int:
            if not root:
                return  0

            maxLeft = max(0, dfs(root.left))
            maxRight = max(0, dfs(root.right))

            self.max_sum = max(self.max_sum, root.val + maxLeft + maxRight)
            noSplitMax = root.val + max(maxLeft, maxRight)
            
            return noSplitMax
        self.max_sum = root.val
        dfs(root)
        return self.max_sum
            
