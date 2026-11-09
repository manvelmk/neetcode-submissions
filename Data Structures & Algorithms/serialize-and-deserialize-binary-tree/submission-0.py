# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    NULL_CHAR = '\0'
    DELIM_CHAR = '|'
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []
        
        def dfs(node: Optional[TreeNode]):
            if node:
                output.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                output.append(self.NULL_CHAR)
        dfs(root)
        return self.DELIM_CHAR.join(output)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data:
            output = data.split(self.DELIM_CHAR)
            self.iterator = 0

            def dfs():
                if self.NULL_CHAR == output[self.iterator]:
                    # skip null node but increment iterator still
                    self.iterator += 1
                    return None
                
                value = int(output[self.iterator])
                self.iterator += 1
                node = TreeNode(value, dfs(), dfs())
                return node
            
            return dfs()
        else:
            return None
