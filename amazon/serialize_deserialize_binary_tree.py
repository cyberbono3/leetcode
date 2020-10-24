"""


297. Serialize and Deserialize Binary Tree
Hard

3527

169

Add to List

Share
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000




"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    pre_index = 0

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        
        
        preorder traversal to serialzie the tree
        "1,2,null,null,3,4,null,null, 5, null, null"
        
        
        
        
        """
        def preorder(node):
            if not node: return "null"
            return str(node.val)  + "," + preorder(node.left)  + ","  + preorder(node.right)
        
        
        if not root:
            return "null"
        if not root.left and not root.right:
            return str(root.val)
            
        s = preorder(root)
        print("s", s)
        return s
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        
        
         "1,2,null,null,3,4,null,null, 5, null, null"
        
                  1
                 
        
        """
        def constructTree():
            if self.pre_index > len(l) -1:
                return None
            
            elif l[self.pre_index] == "null":
                self.pre_index += 1
                return None
            
            val = int(l[self.pre_index])
            self.pre_index += 1
            
            root = TreeNode(val)
            root.left = constructTree()
            root.right = constructTree()
            return root
            
            
            
            
            
        
        if data == "null":
            return None
        if len(data) == 1:
            return TreeNode(int(data[0]))
        
        l = data.split(",")
        return constructTree()
        
        
        
     
     
     
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))