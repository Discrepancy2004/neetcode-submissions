# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        res = 0
        def height(root):
            nonlocal flag
            if root == None:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            if flag and abs(left - right) > 1:
                flag = False
                
            return 1 + max(left,right)
        
        res = height(root)
        return flag
