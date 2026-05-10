# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # result = max(result, left_subtree + right_subtree)
        # height = 1+ max(left_subtree, right_subtree)

        # this is making it the member variable  of class, so it is accessible 
        # inside the nested function
        self.result = 0


        #dfs will return the height
        def dfs(current):
            if not current:
                return 0

            left = dfs(current.left)
            right = dfs(current.right)

            self.result = max(self.result, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.result



        
        