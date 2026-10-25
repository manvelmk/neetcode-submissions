from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        retList: List[List[int]] = []
        queue = deque([root])

        while queue:
            # one layer at a time
            layer = []

            # for each node in the pending queue
            for _ in range(len(queue)):
                node = queue.popleft()
                if node: # make sure to only add valid nodes
                    layer.append(node.val)
                    # queue up subnodes, left to righ
                    queue.append(node.left)
                    queue.append(node.right)
            
            # Problem expects no empty sub layers in output
            if layer:
                retList.append(layer)
        
        return retList
