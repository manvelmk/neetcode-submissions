# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curNode = root

        while curNode:
            if p.val > curNode.val and q.val > curNode.val:
                curNode = curNode.right
            elif p.val < curNode.val and q.val < curNode.val:
                curNode = curNode.left
            else:
                break
        
        return curNode