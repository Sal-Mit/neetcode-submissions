# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = []

        def dfs (node, maxNodeValue):
            if not node:
                return None

            maxNodeValue = max(maxNodeValue, node.val)
            
            if node.val >= maxNodeValue:
                res.append(node.val)

            dfs(node.left, maxNodeValue)
            dfs(node.right, maxNodeValue)

        dfs(root, -999)

        return len(res)
        