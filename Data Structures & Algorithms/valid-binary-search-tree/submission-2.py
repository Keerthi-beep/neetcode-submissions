# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode],mini = float('-inf'), maxi = float('inf')) -> bool:
        if not root:
            return True
        if root.val >= maxi or root.val<=mini:
            return False

        left = self.isValidBST(root.left,mini,root.val)
        right = self.isValidBST(root.right,root.val,maxi)

        return left and right