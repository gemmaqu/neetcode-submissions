# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        sorted = []
        sorted.extend(self.inorderTraversal(root.left)) # expand the value to let the left subtree in
        sorted.append(root.val)
        sorted.extend(self.inorderTraversal(root.right))
       
        return sorted
        