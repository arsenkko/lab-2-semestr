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