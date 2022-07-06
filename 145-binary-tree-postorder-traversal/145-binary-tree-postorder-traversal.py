# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
        
#################################################################################

class Solution:
    def __init__(self):
        self.lst=[]
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root):
            if not root:
                return []
            else:
                postorder(root.left)
                postorder(root.right)
                self.lst.append(root.val)
        postorder(root)
        return self.lst
        