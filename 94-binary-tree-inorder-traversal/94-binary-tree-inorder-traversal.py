# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        else: 
            return self.inorderTraversal(root.left)+                        [root.val]+self.inorderTraversal(root.right)
        
        
        
#################################################################
        
class Solution:
    def __init__(self):
        self.lst=[]
    def inorderTraversal(self, root):
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)                       
            self.lst.append(root.val)
            inorder(root.right)
        inorder(root)    
        return self.lst
        
        
        
       
