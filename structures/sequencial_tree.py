class SequencialTreeNode:
    def __init__(self, key, data1, data2):
        self.key = key
        self.data1 = data1
        self.data2 = data2

class SequentialTree:
    def __init__(self):
        self.tree = []

    def insert(self, key, data1, data2):
        node = SequencialTreeNode(key, data1, data2)
        self.tree.append(node)

    def search_with_count(self, _, key):
        comparisons = 0
        for node in self.tree:
            comparisons += 1
            if node.key == key:
                return node, comparisons
        return None, comparisons