class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root): # the functin we invented 
            if not root:
                return 0
            
            left_height = check(root.left)
            right_height = check(root.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1 #return the height of the root
            #why do we need this return? because we need this to make left_height and right_height meaningful
        
        return check(root) != -1 # if this, return true, otherwise return false