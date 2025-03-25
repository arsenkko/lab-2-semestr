import unittest

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def sum_of_left_leaves(root):
    if not root:
        return 0
    
    total_sum = 0
    
    if root.left_child and not root.left_child.left_child and not root.left_child.right_child:
        total_sum += root.left_child.data
    
    total_sum += sum_of_left_leaves(root.left_child)
    total_sum += sum_of_left_leaves(root.right_child)
    
    return total_sum

class TestSumOfLeftLeaves(unittest.TestCase):
    def test_standard_case(self):
        root = TreeNode(3)
        root.left_child = TreeNode(9)
        root.right_child = TreeNode(20)
        root.right_child.left_child = TreeNode(15)
        root.right_child.right_child = TreeNode(7)
        self.assertEqual(sum_of_left_leaves(root), 24)
    
    def test_left_only_tree(self):
        root = TreeNode(10)
        root.left_child = TreeNode(5)
        root.left_child.left_child = TreeNode(2)
        root.left_child.left_child.left_child = TreeNode(1)
        self.assertEqual(sum_of_left_leaves(root), 1) 
    
    def test_right_only_tree(self):
        root = TreeNode(10)
        root.right_child = TreeNode(20)
        root.right_child.right_child = TreeNode(30)
        root.right_child.right_child.right_child = TreeNode(40)
        self.assertEqual(sum_of_left_leaves(root), 0) 

if __name__ == "__main__":
    unittest.main()