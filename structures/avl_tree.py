class AVLNode:
    def __init__(self, key, data1, data2):
        self.key = key
        self.data1 = data1
        self.data2 = data2
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        
    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def insert(self, node, key, data1, data2):
        if not node:
            return AVLNode(key, data1, data2)

        if key < node.key:
            node.left = self.insert(node.left, key, data1, data2)
        else:
            node.right = self.insert(node.right, key, data1, data2)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def search_with_count(self, node, key):
        comparisons = 0
        while node:
            comparisons += 1
            if key == node.key:
                return node, comparisons
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None, comparisons