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

        # inorder search
        result = []

        def inOrder(root):
            if not root:
                return 
            inOrder(root.left)
            result.append(root.val)
            inOrder(root.right)
        
        inOrder(root)

        for i in range(1, len(result)):
            if not result[i] > result[i-1]:
                return False
        return True
