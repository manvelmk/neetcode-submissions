# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))


    def validate(self, node: Optional[TreeNode], min: float, max: float) -> bool:
        if not node:
            return True

        if node.val <= min or node.val >= max:
            return False
        
        leftIsValid = self.validate(node.left, min, node.val)
        rightIsValid = self.validate(node.right, node.val, max)
        
        return leftIsValid and rightIsValid