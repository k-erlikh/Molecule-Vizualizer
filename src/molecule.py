class Molecule:
    def __init__(self):
        self.vectors = []
    
    def add_element(self, element):
        node = Node()
        init_Node(node, element)
        self.vectors.append(node)
    
    def remove_element(self, node):
        self.vectors.remove(node)

class Node:
    def __init__(self):
        self.element = None
        self.edges = []

def init_Node(node, element):
    node.element = element
