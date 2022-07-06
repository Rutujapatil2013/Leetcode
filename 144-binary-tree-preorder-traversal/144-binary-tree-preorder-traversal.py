# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
        
#################################################################################

class Solution:
    def __init__(self):
        self.lst=[]
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if not root:
                return []
            else:
                self.lst.append(root.val)
                inorder(root.left)
                inorder(root.right)
        inorder(root)
        return self.lst
            
        

            
        