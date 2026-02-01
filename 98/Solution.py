'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

node value type: int
return boolean for if valid 
equal values return false, strictly greater or less


Ex 1
Input: root = [2,1,3]

		2
  /   \
 1     3

Output: true

Ex 2
Input: root = [5,1,4,null,null,3,6]

		5
  /   \
 1     4
      /  \
     3    6

Output: false

'''

class TreeNode:
  val = 0
  left = None
  right = None
  
  def __init__(self, val, left, right):
    self.val = val
    self.left = left
    self.right = right

def validBST(root : TreeNode):
  return validate(root, float("-inf"), float("inf"))
	
  

def validate(node, lowerBound, upperBound):
  # base case
  if not node:
    return True
  
  # validate the node in the range
  if not lowerBound <= node.val <= upperBound:
    return False
  
  # calling the function for the children nodes
  return validate(node.left, lowerBound, node.val -1) and validate(node.right, node.val + 1, upperBound)


# Test cases for provided examples
if __name__ == "__main__":
  root = TreeNode(5,
                 TreeNode(1, None, None),
                 TreeNode(4, TreeNode(3, None, None), TreeNode(6, None, None)))
  print(validBST(root))


######### In order traversal, the nodes would be traversed in sorted order
# if you did the traversal and its sorted, then valid
# would not save the time or space complexity 



