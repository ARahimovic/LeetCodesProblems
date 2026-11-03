class TreeNode :
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


def dfs(node) :
    if not node:
        return
    
    print(node.val)
    dfs(node.left)
    dfs(node.right)


dfs(root)

def max_depth(node) :
    if not node :
        return 0


    return max(max_depth(node.left), max_depth(node.right)) + 1

print("Max depth")
print(max_depth(root))


def reverse_tree(node):
    if not node :
        return 

 
    node.left , node.right = node.right, node.left
    reverse_tree(node.left)
    reverse_tree(node.right)
    
    

def same_Tree(p : TreeNode, q : TreeNode) -> bool :
    if not p and not q :
        return True

    elif not q or not p :
        return False

    elif p.val != q.val : 
        return False

    
    return same_Tree(p.right, q.right) and  same_Tree(p.left, q.left)



from collections import deque :
def travel_order(node):
    if not node :
        return []
    
    orders= []

    queue = deque([(node)])

    while queue :
        node = queue.popleft()
        
        if node == None :
            continue 

        for left, right in node :
            queue.append((left,right))
            order.append((left,right))     



def is_valid_bst(node, low=float('-inf'), high=float('inf')) :
    if not node :
        return True

    if not (low < node.val <high) :
        return False
    
    return is_valid_bst(node.right, node.val, high) and is_valid_bst(node.left, low, node.val)