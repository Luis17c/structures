class BinaryTreeNode:
    def __init__(self, key, data1, data2):
        self.key = key
        self.data1 = data1
        self.data2 = data2
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data1, data2):
        new_node = BinaryTreeNode(key, data1, data2)
        if not self.root:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search_with_count(self, node, key):
        comparisons = 0
        current = node
        while current:
            comparisons += 1
            if key == current.key:
                return current, comparisons
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None, comparisons