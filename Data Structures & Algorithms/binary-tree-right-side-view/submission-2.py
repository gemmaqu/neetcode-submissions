# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()

        if root:
            q.append(root)
        res = []

        
        while q:
            qlen = len(q)
            level = []
            

            for i in range (qlen):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                ll = len(level) # put it here since we want to calculate 
                #the lengeth of level after it is added something

            res.append(level[ll-1]) # the index-1
        return res



        