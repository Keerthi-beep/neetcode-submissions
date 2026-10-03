# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.solve(root,float('-inf'),float('inf'))

    def solve(self,root,mini,maxi):
        if not root:
            return True
        if root.val >= maxi or root.val<=mini:
            return False

        left = self.solve(root.left,mini,root.val)
        right = self.solve(root.right,root.val,maxi)

        return left and right