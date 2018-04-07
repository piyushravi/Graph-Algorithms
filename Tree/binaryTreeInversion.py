# Problem at https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root, flag = True):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root!=None:
            root.left, root.right = root.right, root.left
            
            if root.right!=None:
                self.invertTree(root.right, False)
        
            if root.left!=None:
                self.invertTree(root.left, False)
        
        if flag:
            return root
        
    def result(self, root):
        res = []
        
        toVisit = []
        if root!=None:
            toVisit = [root]
        
        for x in toVisit:
            
            if x!=None:
                toVisit.append(x.left)
                toVisit.append(x.right)
            
                res.append(x.val)
            
            else:
                res.append(None)
          
        ctr = 0
        n = len(res)
        for x in xrange(n):
            if res[n-x-1]!=None:
                break
            
            ctr+=1
        
        res = res[:n-ctr]
        
        return res
        
    
        
        
        
